## Code From Google sentencepices

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='sentencepiece_model.proto',
    package='sentencepiece',
    syntax='proto2',
    serialized_options=b'H\003',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x19sentencepiece_model.proto\x12\rsentencepiece\"\xdb\x0b\n\x0bTrainerSpec\x12\r\n\x05input\x18\x01 \x03(\t\x12\x14\n\x0cinput_format\x18\x07 \x01(\t\x12\x14\n\x0cmodel_prefix\x18\x02 \x01(\t\x12\x41\n\nmodel_type\x18\x03 \x01(\x0e\x32$.sentencepiece.TrainerSpec.ModelType:\x07UNIGRAM\x12\x18\n\nvocab_size\x18\x04 \x01(\x05:\x04\x38\x30\x30\x30\x12\x17\n\x0f\x61\x63\x63\x65pt_language\x18\x05 \x03(\t\x12 \n\x15self_test_sample_size\x18\x06 \x01(\x05:\x01\x30\x12*\n\x1b\x65nable_differential_privacy\x18\x32 \x01(\x08:\x05\x66\x61lse\x12+\n differential_privacy_noise_level\x18\x33 \x01(\x02:\x01\x30\x12\x32\n\'differential_privacy_clipping_threshold\x18\x34 \x01(\x04:\x01\x30\x12\"\n\x12\x63haracter_coverage\x18\n \x01(\x02:\x06\x30.9995\x12\x1e\n\x13input_sentence_size\x18\x0b \x01(\x04:\x01\x30\x12$\n\x16shuffle_input_sentence\x18\x13 \x01(\x08:\x04true\x12 \n\x14mining_sentence_size\x18\x0c \x01(\x05\x42\x02\x18\x01\x12\"\n\x16training_sentence_size\x18\r \x01(\x05\x42\x02\x18\x01\x12(\n\x17seed_sentencepiece_size\x18\x0e \x01(\x05:\x07\x31\x30\x30\x30\x30\x30\x30\x12\x1e\n\x10shrinking_factor\x18\x0f \x01(\x02:\x04\x30.75\x12!\n\x13max_sentence_length\x18\x12 \x01(\x05:\x04\x34\x31\x39\x32\x12\x17\n\x0bnum_threads\x18\x10 \x01(\x05:\x02\x31\x36\x12\x1d\n\x12num_sub_iterations\x18\x11 \x01(\x05:\x01\x32\x12$\n\x18max_sentencepiece_length\x18\x14 \x01(\x05:\x02\x31\x36\x12%\n\x17split_by_unicode_script\x18\x15 \x01(\x08:\x04true\x12\x1d\n\x0fsplit_by_number\x18\x17 \x01(\x08:\x04true\x12!\n\x13split_by_whitespace\x18\x16 \x01(\x08:\x04true\x12)\n\x1atreat_whitespace_as_suffix\x18\x18 \x01(\x08:\x05\x66\x61lse\x12+\n\x1c\x61llow_whitespace_only_pieces\x18\x1a \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0csplit_digits\x18\x19 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x0f\x63ontrol_symbols\x18\x1e \x03(\t\x12\x1c\n\x14user_defined_symbols\x18\x1f \x03(\t\x12\x16\n\x0erequired_chars\x18$ \x01(\t\x12\x1c\n\rbyte_fallback\x18# \x01(\x08:\x05\x66\x61lse\x12+\n\x1dvocabulary_output_piece_score\x18  \x01(\x08:\x04true\x12\x1e\n\x10hard_vocab_limit\x18! \x01(\x08:\x04true\x12\x1c\n\ruse_all_vocab\x18\" \x01(\x08:\x05\x66\x61lse\x12\x11\n\x06unk_id\x18( \x01(\x05:\x01\x30\x12\x11\n\x06\x62os_id\x18) \x01(\x05:\x01\x31\x12\x11\n\x06\x65os_id\x18* \x01(\x05:\x01\x32\x12\x12\n\x06pad_id\x18+ \x01(\x05:\x02-1\x12\x18\n\tunk_piece\x18- \x01(\t:\x05<unk>\x12\x16\n\tbos_piece\x18. \x01(\t:\x03<s>\x12\x17\n\teos_piece\x18/ \x01(\t:\x04</s>\x12\x18\n\tpad_piece\x18\x30 \x01(\t:\x05<pad>\x12\x1a\n\x0bunk_surface\x18, \x01(\t:\x05 \xe2\x81\x87 \x12+\n\x1ctrain_extremely_large_corpus\x18\x31 \x01(\x08:\x05\x66\x61lse\"5\n\tModelType\x12\x0b\n\x07UNIGRAM\x10\x01\x12\x07\n\x03\x42PE\x10\x02\x12\x08\n\x04WORD\x10\x03\x12\x08\n\x04\x43HAR\x10\x04*\t\x08\xc8\x01\x10\x80\x80\x80\x80\x02\"\xd1\x01\n\x0eNormalizerSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x14precompiled_charsmap\x18\x02 \x01(\x0c\x12\x1e\n\x10\x61\x64\x64_dummy_prefix\x18\x03 \x01(\x08:\x04true\x12&\n\x18remove_extra_whitespaces\x18\x04 \x01(\x08:\x04true\x12 \n\x12\x65scape_whitespaces\x18\x05 \x01(\x08:\x04true\x12\x1e\n\x16normalization_rule_tsv\x18\x06 \x01(\t*\t\x08\xc8\x01\x10\x80\x80\x80\x80\x02\"y\n\x0cSelfTestData\x12\x33\n\x07samples\x18\x01 \x03(\x0b\x32\".sentencepiece.SelfTestData.Sample\x1a)\n\x06Sample\x12\r\n\x05input\x18\x01 \x01(\t\x12\x10\n\x08\x65xpected\x18\x02 \x01(\t*\t\x08\xc8\x01\x10\x80\x80\x80\x80\x02\"\xfe\x03\n\nModelProto\x12\x37\n\x06pieces\x18\x01 \x03(\x0b\x32\'.sentencepiece.ModelProto.SentencePiece\x12\x30\n\x0ctrainer_spec\x18\x02 \x01(\x0b\x32\x1a.sentencepiece.TrainerSpec\x12\x36\n\x0fnormalizer_spec\x18\x03 \x01(\x0b\x32\x1d.sentencepiece.NormalizerSpec\x12\x33\n\x0eself_test_data\x18\x04 \x01(\x0b\x32\x1b.sentencepiece.SelfTestData\x12\x38\n\x11\x64\x65normalizer_spec\x18\x05 \x01(\x0b\x32\x1d.sentencepiece.NormalizerSpec\x1a\xd2\x01\n\rSentencePiece\x12\r\n\x05piece\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x42\n\x04type\x18\x03 \x01(\x0e\x32,.sentencepiece.ModelProto.SentencePiece.Type:\x06NORMAL\"T\n\x04Type\x12\n\n\x06NORMAL\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x12\x0b\n\x07\x43ONTROL\x10\x03\x12\x10\n\x0cUSER_DEFINED\x10\x04\x12\x08\n\x04\x42YTE\x10\x06\x12\n\n\x06UNUSED\x10\x05*\t\x08\xc8\x01\x10\x80\x80\x80\x80\x02*\t\x08\xc8\x01\x10\x80\x80\x80\x80\x02\x42\x02H\x03'
)

_TRAINERSPEC_MODELTYPE = _descriptor.EnumDescriptor(
    name='ModelType',
    full_name='sentencepiece.TrainerSpec.ModelType',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNIGRAM', index=0, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='BPE', index=1, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='WORD', index=2, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='CHAR', index=3, number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1480,
    serialized_end=1533,
)
_sym_db.RegisterEnumDescriptor(_TRAINERSPEC_MODELTYPE)

_MODELPROTO_SENTENCEPIECE_TYPE = _descriptor.EnumDescriptor(
    name='Type',
    full_name='sentencepiece.ModelProto.SentencePiece.Type',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='NORMAL', index=0, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN', index=1, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='CONTROL', index=2, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='USER_DEFINED', index=3, number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='BYTE', index=4, number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='UNUSED', index=5, number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=2286,
    serialized_end=2370,
)
_sym_db.RegisterEnumDescriptor(_MODELPROTO_SENTENCEPIECE_TYPE)

_TRAINERSPEC = _descriptor.Descriptor(
    name='TrainerSpec',
    full_name='sentencepiece.TrainerSpec',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='input', full_name='sentencepiece.TrainerSpec.input', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='input_format', full_name='sentencepiece.TrainerSpec.input_format', index=1,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='model_prefix', full_name='sentencepiece.TrainerSpec.model_prefix', index=2,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='model_type', full_name='sentencepiece.TrainerSpec.model_type', index=3,
            number=3, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='vocab_size', full_name='sentencepiece.TrainerSpec.vocab_size', index=4,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=8000,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='accept_language', full_name='sentencepiece.TrainerSpec.accept_language', index=5,
            number=5, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='self_test_sample_size', full_name='sentencepiece.TrainerSpec.self_test_sample_size', index=6,
            number=6, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='enable_differential_privacy', full_name='sentencepiece.TrainerSpec.enable_differential_privacy',
            index=7,
            number=50, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='differential_privacy_noise_level',
            full_name='sentencepiece.TrainerSpec.differential_privacy_noise_level', index=8,
            number=51, type=2, cpp_type=6, label=1,
            has_default_value=True, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='differential_privacy_clipping_threshold',
            full_name='sentencepiece.TrainerSpec.differential_privacy_clipping_threshold', index=9,
            number=52, type=4, cpp_type=4, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='character_coverage', full_name='sentencepiece.TrainerSpec.character_coverage', index=10,
            number=10, type=2, cpp_type=6, label=1,
            has_default_value=True, default_value=float(0.9995),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='input_sentence_size', full_name='sentencepiece.TrainerSpec.input_sentence_size', index=11,
            number=11, type=4, cpp_type=4, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='shuffle_input_sentence', full_name='sentencepiece.TrainerSpec.shuffle_input_sentence', index=12,
            number=19, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='mining_sentence_size', full_name='sentencepiece.TrainerSpec.mining_sentence_size', index=13,
            number=12, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=b'\030\001', file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='training_sentence_size', full_name='sentencepiece.TrainerSpec.training_sentence_size', index=14,
            number=13, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=b'\030\001', file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='seed_sentencepiece_size', full_name='sentencepiece.TrainerSpec.seed_sentencepiece_size', index=15,
            number=14, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=1000000,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='shrinking_factor', full_name='sentencepiece.TrainerSpec.shrinking_factor', index=16,
            number=15, type=2, cpp_type=6, label=1,
            has_default_value=True, default_value=float(0.75),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='max_sentence_length', full_name='sentencepiece.TrainerSpec.max_sentence_length', index=17,
            number=18, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=4192,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='num_threads', full_name='sentencepiece.TrainerSpec.num_threads', index=18,
            number=16, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=16,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='num_sub_iterations', full_name='sentencepiece.TrainerSpec.num_sub_iterations', index=19,
            number=17, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=2,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='max_sentencepiece_length', full_name='sentencepiece.TrainerSpec.max_sentencepiece_length', index=20,
            number=20, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=16,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='split_by_unicode_script', full_name='sentencepiece.TrainerSpec.split_by_unicode_script', index=21,
            number=21, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='split_by_number', full_name='sentencepiece.TrainerSpec.split_by_number', index=22,
            number=23, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='split_by_whitespace', full_name='sentencepiece.TrainerSpec.split_by_whitespace', index=23,
            number=22, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='treat_whitespace_as_suffix', full_name='sentencepiece.TrainerSpec.treat_whitespace_as_suffix',
            index=24,
            number=24, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='allow_whitespace_only_pieces', full_name='sentencepiece.TrainerSpec.allow_whitespace_only_pieces',
            index=25,
            number=26, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='split_digits', full_name='sentencepiece.TrainerSpec.split_digits', index=26,
            number=25, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='control_symbols', full_name='sentencepiece.TrainerSpec.control_symbols', index=27,
            number=30, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='user_defined_symbols', full_name='sentencepiece.TrainerSpec.user_defined_symbols', index=28,
            number=31, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='required_chars', full_name='sentencepiece.TrainerSpec.required_chars', index=29,
            number=36, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='byte_fallback', full_name='sentencepiece.TrainerSpec.byte_fallback', index=30,
            number=35, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='vocabulary_output_piece_score', full_name='sentencepiece.TrainerSpec.vocabulary_output_piece_score',
            index=31,
            number=32, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='hard_vocab_limit', full_name='sentencepiece.TrainerSpec.hard_vocab_limit', index=32,
            number=33, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='use_all_vocab', full_name='sentencepiece.TrainerSpec.use_all_vocab', index=33,
            number=34, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='unk_id', full_name='sentencepiece.TrainerSpec.unk_id', index=34,
            number=40, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='bos_id', full_name='sentencepiece.TrainerSpec.bos_id', index=35,
            number=41, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='eos_id', full_name='sentencepiece.TrainerSpec.eos_id', index=36,
            number=42, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=2,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='pad_id', full_name='sentencepiece.TrainerSpec.pad_id', index=37,
            number=43, type=5, cpp_type=1, label=1,
            has_default_value=True, default_value=-1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='unk_piece', full_name='sentencepiece.TrainerSpec.unk_piece', index=38,
            number=45, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=b"<unk>".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='bos_piece', full_name='sentencepiece.TrainerSpec.bos_piece', index=39,
            number=46, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=b"<s>".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='eos_piece', full_name='sentencepiece.TrainerSpec.eos_piece', index=40,
            number=47, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=b"</s>".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='pad_piece', full_name='sentencepiece.TrainerSpec.pad_piece', index=41,
            number=48, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=b"<pad>".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='unk_surface', full_name='sentencepiece.TrainerSpec.unk_surface', index=42,
            number=44, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=b" \342\201\207 ".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='train_extremely_large_corpus', full_name='sentencepiece.TrainerSpec.train_extremely_large_corpus',
            index=43,
            number=49, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _TRAINERSPEC_MODELTYPE,
    ],
    serialized_options=None,
    is_extendable=True,
    syntax='proto2',
    extension_ranges=[(200, 536870912), ],
    oneofs=[
    ],
    serialized_start=45,
    serialized_end=1544,
)

_NORMALIZERSPEC = _descriptor.Descriptor(
    name='NormalizerSpec',
    full_name='sentencepiece.NormalizerSpec',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='sentencepiece.NormalizerSpec.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='precompiled_charsmap', full_name='sentencepiece.NormalizerSpec.precompiled_charsmap', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=b"",
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='add_dummy_prefix', full_name='sentencepiece.NormalizerSpec.add_dummy_prefix', index=2,
            number=3, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='remove_extra_whitespaces', full_name='sentencepiece.NormalizerSpec.remove_extra_whitespaces', index=3,
            number=4, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='escape_whitespaces', full_name='sentencepiece.NormalizerSpec.escape_whitespaces', index=4,
            number=5, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=True,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='normalization_rule_tsv', full_name='sentencepiece.NormalizerSpec.normalization_rule_tsv', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=True,
    syntax='proto2',
    extension_ranges=[(200, 536870912), ],
    oneofs=[
    ],
    serialized_start=1547,
    serialized_end=1756,
)

_SELFTESTDATA_SAMPLE = _descriptor.Descriptor(
    name='Sample',
    full_name='sentencepiece.SelfTestData.Sample',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='input', full_name='sentencepiece.SelfTestData.Sample.input', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='expected', full_name='sentencepiece.SelfTestData.Sample.expected', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1827,
    serialized_end=1868,
)

_SELFTESTDATA = _descriptor.Descriptor(
    name='SelfTestData',
    full_name='sentencepiece.SelfTestData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='samples', full_name='sentencepiece.SelfTestData.samples', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[_SELFTESTDATA_SAMPLE, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=True,
    syntax='proto2',
    extension_ranges=[(200, 536870912), ],
    oneofs=[
    ],
    serialized_start=1758,
    serialized_end=1879,
)

_MODELPROTO_SENTENCEPIECE = _descriptor.Descriptor(
    name='SentencePiece',
    full_name='sentencepiece.ModelProto.SentencePiece',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='piece', full_name='sentencepiece.ModelProto.SentencePiece.piece', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='score', full_name='sentencepiece.ModelProto.SentencePiece.score', index=1,
            number=2, type=2, cpp_type=6, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='type', full_name='sentencepiece.ModelProto.SentencePiece.type', index=2,
            number=3, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _MODELPROTO_SENTENCEPIECE_TYPE,
    ],
    serialized_options=None,
    is_extendable=True,
    syntax='proto2',
    extension_ranges=[(200, 536870912), ],
    oneofs=[
    ],
    serialized_start=2171,
    serialized_end=2381,
)

_MODELPROTO = _descriptor.Descriptor(
    name='ModelProto',
    full_name='sentencepiece.ModelProto',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='pieces', full_name='sentencepiece.ModelProto.pieces', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='trainer_spec', full_name='sentencepiece.ModelProto.trainer_spec', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='normalizer_spec', full_name='sentencepiece.ModelProto.normalizer_spec', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='self_test_data', full_name='sentencepiece.ModelProto.self_test_data', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='denormalizer_spec', full_name='sentencepiece.ModelProto.denormalizer_spec', index=4,
            number=5, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[_MODELPROTO_SENTENCEPIECE, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=True,
    syntax='proto2',
    extension_ranges=[(200, 536870912), ],
    oneofs=[
    ],
    serialized_start=1882,
    serialized_end=2392,
)

_TRAINERSPEC.fields_by_name['model_type'].enum_type = _TRAINERSPEC_MODELTYPE
_TRAINERSPEC_MODELTYPE.containing_type = _TRAINERSPEC
_SELFTESTDATA_SAMPLE.containing_type = _SELFTESTDATA
_SELFTESTDATA.fields_by_name['samples'].message_type = _SELFTESTDATA_SAMPLE
_MODELPROTO_SENTENCEPIECE.fields_by_name['type'].enum_type = _MODELPROTO_SENTENCEPIECE_TYPE
_MODELPROTO_SENTENCEPIECE.containing_type = _MODELPROTO
_MODELPROTO_SENTENCEPIECE_TYPE.containing_type = _MODELPROTO_SENTENCEPIECE
_MODELPROTO.fields_by_name['pieces'].message_type = _MODELPROTO_SENTENCEPIECE
_MODELPROTO.fields_by_name['trainer_spec'].message_type = _TRAINERSPEC
_MODELPROTO.fields_by_name['normalizer_spec'].message_type = _NORMALIZERSPEC
_MODELPROTO.fields_by_name['self_test_data'].message_type = _SELFTESTDATA
_MODELPROTO.fields_by_name['denormalizer_spec'].message_type = _NORMALIZERSPEC
DESCRIPTOR.message_types_by_name['TrainerSpec'] = _TRAINERSPEC
DESCRIPTOR.message_types_by_name['NormalizerSpec'] = _NORMALIZERSPEC
DESCRIPTOR.message_types_by_name['SelfTestData'] = _SELFTESTDATA
DESCRIPTOR.message_types_by_name['ModelProto'] = _MODELPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainerSpec = _reflection.GeneratedProtocolMessageType('TrainerSpec', (_message.Message,), {
    'DESCRIPTOR': _TRAINERSPEC,
    '__module__': 'sentencepiece_model_pb2'
    # @@protoc_insertion_point(class_scope:sentencepiece.TrainerSpec)
})
_sym_db.RegisterMessage(TrainerSpec)

NormalizerSpec = _reflection.GeneratedProtocolMessageType('NormalizerSpec', (_message.Message,), {
    'DESCRIPTOR': _NORMALIZERSPEC,
    '__module__': 'sentencepiece_model_pb2'
    # @@protoc_insertion_point(class_scope:sentencepiece.NormalizerSpec)
})
_sym_db.RegisterMessage(NormalizerSpec)

SelfTestData = _reflection.GeneratedProtocolMessageType('SelfTestData', (_message.Message,), {

    'Sample': _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), {
        'DESCRIPTOR': _SELFTESTDATA_SAMPLE,
        '__module__': 'sentencepiece_model_pb2'
        # @@protoc_insertion_point(class_scope:sentencepiece.SelfTestData.Sample)
    })
    ,
    'DESCRIPTOR': _SELFTESTDATA,
    '__module__': 'sentencepiece_model_pb2'
    # @@protoc_insertion_point(class_scope:sentencepiece.SelfTestData)
})
_sym_db.RegisterMessage(SelfTestData)
_sym_db.RegisterMessage(SelfTestData.Sample)

ModelProto = _reflection.GeneratedProtocolMessageType('ModelProto', (_message.Message,), {

    'SentencePiece': _reflection.GeneratedProtocolMessageType('SentencePiece', (_message.Message,), {
        'DESCRIPTOR': _MODELPROTO_SENTENCEPIECE,
        '__module__': 'sentencepiece_model_pb2'
        # @@protoc_insertion_point(class_scope:sentencepiece.ModelProto.SentencePiece)
    })
    ,
    'DESCRIPTOR': _MODELPROTO,
    '__module__': 'sentencepiece_model_pb2'
    # @@protoc_insertion_point(class_scope:sentencepiece.ModelProto)
})
_sym_db.RegisterMessage(ModelProto)
_sym_db.RegisterMessage(ModelProto.SentencePiece)

DESCRIPTOR._options = None
_TRAINERSPEC.fields_by_name['mining_sentence_size']._options = None
_TRAINERSPEC.fields_by_name['training_sentence_size']._options = None
# @@protoc_insertion_point(module_scope)
