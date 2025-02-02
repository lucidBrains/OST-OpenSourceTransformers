import json
import os
from logging import getLogger
from typing import Optional, List, Union

import torch
import transformers
from torch.utils.data import Dataset
from tqdm.auto import tqdm

logger = getLogger(__name__)

__all__ = ['Tokens', 'ManualDataSet', 'DatasetPGTChat', 'DatasetLGeM', 'DatasetLLMoU', 'DatasetLLmP', 'DatasetLLmPU',
           'DatasetLLmPChat', 'DatasetLLama', 'CasualLMDataset']


def prompt_to_instruction(instruction, input_=None, response_=None, eos='<|endoftext|>'):
    if input_ is None:
        st1_prompting = f'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n\n{instruction}\n\n'
    else:
        st1_prompting = f'Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\n\n{instruction}\n\n### Input:\n\n{input_}\n\n'
    resp = f'### Response:\n\n{response_}{eos}' if response_ is not None else '### Response:\n\n'
    return st1_prompting + resp


class Tokens:
    eos = '<|endoftext|>'
    pad = '<|pad|>'
    sos = '<|startoftext|>'
    atn_start = '<|STN|>'
    atn_end = '<|ETN|>'


class ManualDataSet:
    def pre_processing(self, inp):
        return NotImplemented


class CasualLMDataset(Dataset, ManualDataSet):

    def __init__(self, data: List[dict],
                 tokenizer: Optional[transformers.PreTrainedTokenizer], max_length: Optional[int] = 128):
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
        self.tokenizer = tokenizer
        self.attention_mask = []
        self.input_ids = []
        self.max_length = max_length
        preprocessed_data = []
        for dict_ in tqdm(data):
            instruction = dict_['instruction']
            inpt = dict_['input']
            output = dict_['output']
            string = prompt_to_instruction(instruction=instruction, input_=inpt if inpt != '' else None,
                                           response_=output, eos=tokenizer.eos_token)
            preprocessed_data.append(string)
        tqdm_pr = tqdm(iterable=preprocessed_data)
        for string in tqdm_pr:
            encodings_dict = tokenizer.encode_plus(string, max_length=max_length, truncation=True,
                                                   return_tensors='pt',
                                                   padding="max_length")
            self.attention_mask.append(encodings_dict['attention_mask'])
            self.input_ids.append(encodings_dict['input_ids'])

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attention_mask[idx]

    def pre_processing(self, inp):

        return self.tokenizer.encode_plus(prompt_to_instruction(inp), max_length=self.max_length, truncation=True,
                                          return_tensors='pt',
                                          padding="max_length")

    def encode(self, text):
        enc_trg = self.tokenizer.encode_plus(
            text=text,
            max_length=self.max_length,
            padding='do_not_pad',
            add_special_tokens=True,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        return enc_trg


class DatasetLLmPU(Dataset):
    def __init__(self, tokenizer, source_len, target_len, source_text, target_text):
        self.tokenizer = tokenizer
        self.source_len = source_len
        self.target_len = target_len
        self.target_text = target_text
        self.source_text = source_text

    def __len__(self):
        return len(self.target_text)

    def __getitem__(self, index) -> dict:
        """
        :param index:
        :return: 'source_ids','source_mask','target_ids'
        """
        source_text = str(self.source_text[index])
        target_text = str(self.target_text[index])

        source_text = ' '.join(source_text.split())
        target_text = ' '.join(target_text.split())

        source = self.tokenizer.batch_encode_plus([source_text], max_length=self.source_len, pad_to_max_length=True,
                                                  truncation=True, padding="max_length", return_tensors='pt')
        target = self.tokenizer.batch_encode_plus([target_text], max_length=self.target_len, pad_to_max_length=True,
                                                  truncation=True, padding="max_length", return_tensors='pt')

        source_ids = source['input_ids']
        source_mask = source['attention_mask']
        target_ids = target['input_ids']

        return {
            'source_ids': source_ids.to(dtype=torch.long),
            'source_mask': source_mask.to(dtype=torch.long),
            'target_ids': target_ids.to(dtype=torch.long),
        }


class DatasetLLama(Dataset, Tokens):
    def __init__(self, data: Optional[List[str]],
                 tokenizer: Optional[transformers.PreTrainedTokenizer], max_length: Optional[int] = 768):
        self.tokenizer = tokenizer

        self.input_ids = []
        self.max_length = max_length
        logger.info('Tokenizing Data')
        pbar = tqdm(enumerate(data))
        failed = 0
        for i, txt in pbar:
            if txt != '' and not txt.startswith(' ='):
                pbar.set_postfix(failed=failed, collected=i + 1 - failed)

                encodings_dict = tokenizer(self.sos + txt + self.eos, truncation=True,
                                           max_length=max_length, padding="do_not_pad")

                self.input_ids.append(torch.tensor(encodings_dict['input_ids']))
            else:
                failed += 1

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx]

    def encode(self, text):
        enc_trg = self.tokenizer.encode_plus(
            text=text,
            max_length=self.max_length,
            padding='do_not_pad',
            add_special_tokens=True,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        return enc_trg


class DatasetLLmP(Dataset, Tokens):
    def __init__(self, data: Union[dict[List], str], task: str,
                 tokenizer: Optional[transformers.PreTrainedTokenizer], max_length: Optional[int] = 256,
                 till: Optional[int] = 5000):
        self.tokenizer = tokenizer

        tokenizer.add_special_tokens(
            {'pad_token': self.pad, 'eos_token': self.eos, 'bos_token': self.sos}
        )
        if not os.path.exists('tokenizer_model/LLmP-C'):
            os.mkdir('tokenizer_model/LLmP-C')
        agent = '<LLmP> :'
        self.agent = agent
        self.attention_mask = []
        self.input_ids = []
        self.max_length = max_length
        chosen = data['train']
        till = till if till is not None else len(chosen)
        tqdm_pr = tqdm(iterable=enumerate(chosen), total=till)
        for ia, dt in tqdm_pr:
            string = f'{task}\n{dt["input"]}{agent}{dt["output"]["answer"]}{self.eos}'
            encodings_dict = tokenizer.encode_plus(string, max_length=max_length, truncation=True, return_tensors='pt',
                                                   padding="max_length")
            self.attention_mask.append(encodings_dict['attention_mask'])
            self.input_ids.append(encodings_dict['input_ids'])
            if ia == till:
                break

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attention_mask[idx]

    def encode(self, text):
        enc_trg = self.tokenizer.encode_plus(
            text=text,
            max_length=self.max_length,
            padding='do_not_pad',
            add_special_tokens=True,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        return enc_trg


class DatasetLLmPChat(Dataset, Tokens):
    def __init__(self, data: Union[os.PathLike, str], task: str,
                 tokenizer: Optional[transformers.PreTrainedTokenizer], max_length: Optional[int] = 128):
        self.tokenizer = tokenizer
        # tokenizer.add_special_tokens(
        #     {'pad_token': self.pad, 'eos_token': self.eos, 'bos_token': self.sos}
        # )
        # if not os.path.exists('tokenizer_model/LLmP-C'):
        #     os.mkdir('tokenizer_model/LLmP-C')
        # tokenizer.add_tokens('<LLmP> :')
        # tokenizer.save_pretrained('tokenizer_model/LLmP-C')
        self.attention_mask = []
        self.agent = '<LLmP> :'
        self.input_ids = []
        self.max_length = max_length
        data = json.load(open(data, 'r'))
        conv = []
        for S in data:
            for c in S['dialog']:
                conv.append(c['text'])
        tqdm_pr = tqdm(iterable=range(len(conv)))
        tqdm_pr.set_description('Cleaning Data ')
        preprocessed_data = []
        for c in tqdm_pr:
            try:
                preprocessed_data.append(task + '\n' + conv[c] + '<LLmP> :' + conv[c + 1] + self.eos)
            except IndexError:
                pass
        tqdm_pr = tqdm(iterable=preprocessed_data)
        for string in tqdm_pr:
            encodings_dict = tokenizer.encode_plus(string, max_length=max_length, truncation=True, return_tensors='pt',
                                                   padding="max_length")
            self.attention_mask.append(encodings_dict['attention_mask'])
            self.input_ids.append(encodings_dict['input_ids'])

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attention_mask[idx]

    def encode(self, text):
        enc_trg = self.tokenizer.encode_plus(
            text=text,
            max_length=self.max_length,
            padding='do_not_pad',
            add_special_tokens=True,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        return enc_trg


class DatasetLGeM(Dataset, Tokens, ManualDataSet):
    def __init__(self, data: List[dict],
                 tokenizer: Optional[transformers.PreTrainedTokenizer], max_length: Optional[int] = 128):

        self.tokenizer = tokenizer
        self.attention_mask = []
        self.input_ids = []
        self.max_length = max_length
        preprocessed_data = []
        for dict_ in tqdm(data):
            instruction = dict_['instruction']
            inpt = dict_['input']
            output = dict_['output']
            if inpt == "":
                string = f'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n\n{instruction}\n\n### Response:\n\n{output}{self.eos}'
            else:
                string = f'Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\n\n{instruction}\n\n### Input:\n\n{inpt}\n\n### Response:\n\n{output}{self.eos}'
            preprocessed_data.append(string)
        tqdm_pr = tqdm(iterable=preprocessed_data)
        for string in tqdm_pr:
            encodings_dict = tokenizer.encode_plus(string, max_length=max_length, truncation=True, return_tensors='pt',
                                                   padding="max_length")
            self.attention_mask.append(encodings_dict['attention_mask'])
            self.input_ids.append(encodings_dict['input_ids'])

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attention_mask[idx]

    def pre_processing(self, inp):
        pre = 'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n\n'
        post = '\n\n### Response:\n\n'
        return self.tokenizer.encode_plus(pre + inp + post, max_length=self.max_length, truncation=True,
                                          return_tensors='pt',
                                          padding="max_length")

    def encode(self, text):
        enc_trg = self.tokenizer.encode_plus(
            text=text,
            max_length=self.max_length,
            padding='do_not_pad',
            add_special_tokens=True,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        return enc_trg


class DatasetLLMoU(Dataset, Tokens):
    def __init__(self, data: Union[dict[List], str],
                 tokenizer: Optional[transformers.PreTrainedTokenizer], max_length: Optional[int] = 256,
                 till: Optional[int] = 5000):
        self.tokenizer = tokenizer

        tokenizer.add_special_tokens(
            {'pad_token': self.pad, 'eos_token': self.eos, 'bos_token': self.sos}
        )
        if not os.path.exists('tokenizer_model/LLMoU-C'):
            os.mkdir('tokenizer_model/LLMoU-C')
        agent = '<LLMoU> :'
        self.agent = agent
        paragraph = 'paragraph:'
        question = 'question:'

        self.attention_mask = []
        self.input_ids = []
        self.max_length = max_length
        chosen = data['train']
        till = till if till is not None else len(chosen)
        tqdm_pr = tqdm(iterable=enumerate(chosen), total=till * 2)
        for ia, dt in tqdm_pr:

            string = f'{paragraph} {dt["paragraph"]} {question} {dt["question"]} {agent} {dt["answer"]} {self.eos}'
            encodings_dict = tokenizer.encode_plus(string, max_length=max_length, truncation=True,
                                                   return_tensors='pt',
                                                   padding="max_length")
            self.attention_mask.append(encodings_dict['attention_mask'])
            self.input_ids.append(encodings_dict['input_ids'])
            if ia == till:
                break

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attention_mask[idx]

    def encode(self, text):
        enc_trg = self.tokenizer.encode_plus(
            text=text,
            max_length=self.max_length,
            padding='do_not_pad',
            add_special_tokens=True,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        return enc_trg


class DatasetPGTChat(Dataset, Tokens):
    def __init__(self, data: Union[os.PathLike, str], task: str,
                 tokenizer: Optional[transformers.PreTrainedTokenizer], max_length: Optional[int] = 128):
        self.tokenizer = tokenizer
        self.agent = '<PGT> :'
        tokenizer.add_special_tokens(
            {'pad_token': self.pad, 'eos_token': self.eos, 'bos_token': self.sos}
        )
        if not os.path.exists('tokenizer_model/PGT-C'):
            os.mkdir('tokenizer_model/PGT-C')

        self.attention_mask = []

        self.input_ids = []
        self.max_length = max_length
        data = json.load(open(data, 'r'))
        conv = []
        for S in data:
            for c in S['dialog']:
                conv.append(c['text'])
        tqdm_pr = tqdm(iterable=range(len(conv)))
        tqdm_pr.set_description('Cleaning Data ')
        preprocessed_data = []
        for c in tqdm_pr:
            try:
                preprocessed_data.append(task + '\n' + conv[c] + self.agent + conv[c + 1] + self.eos)
            except IndexError:
                pass
        tqdm_pr = tqdm(iterable=preprocessed_data)
        for string in tqdm_pr:
            encodings_dict = tokenizer.encode_plus(string, max_length=max_length, truncation=True, return_tensors='pt',
                                                   padding="max_length")
            self.attention_mask.append(encodings_dict['attention_mask'])
            self.input_ids.append(encodings_dict['input_ids'])

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attention_mask[idx]

    def encode(self, text):
        enc_trg = self.tokenizer.encode_plus(
            text=text,
            max_length=self.max_length,
            padding='do_not_pad',
            add_special_tokens=True,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        return enc_trg
