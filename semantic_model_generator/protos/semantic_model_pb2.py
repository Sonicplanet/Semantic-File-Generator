# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_model.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14semantic_model.proto\x12\x18semantic_model_generator\x1a google/protobuf/descriptor.proto\"\xa0\x01\n\tDimension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x08synonyms\x18\x02 \x03(\tB\x04\x90\x82\x19\x01\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\x90\x82\x19\x01\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\t\x12\x14\n\x06unique\x18\x06 \x01(\x08\x42\x04\x90\x82\x19\x01\x12\x1b\n\rsample_values\x18\x07 \x03(\tB\x04\x90\x82\x19\x01\"\xa4\x01\n\rTimeDimension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x08synonyms\x18\x02 \x03(\tB\x04\x90\x82\x19\x01\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\x90\x82\x19\x01\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\t\x12\x14\n\x06unique\x18\x06 \x01(\x08\x42\x04\x90\x82\x19\x01\x12\x1b\n\rsample_values\x18\x07 \x03(\tB\x04\x90\x82\x19\x01\"\xd6\x01\n\x07Measure\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x08synonyms\x18\x02 \x03(\tB\x04\x90\x82\x19\x01\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\x90\x82\x19\x01\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\t\x12L\n\x13\x64\x65\x66\x61ult_aggregation\x18\x06 \x01(\x0e\x32).semantic_model_generator.AggregationTypeB\x04\x90\x82\x19\x01\x12\x1b\n\rsample_values\x18\x07 \x03(\tB\x04\x90\x82\x19\x01\"\\\n\x0bNamedFilter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x08synonyms\x18\x02 \x03(\tB\x04\x90\x82\x19\x01\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\x90\x82\x19\x01\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\"F\n\x13\x46ullyQualifiedTable\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\"\xc4\x03\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x08synonyms\x18\x02 \x03(\tB\x04\x90\x82\x19\x01\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\x90\x82\x19\x01\x12\x41\n\nbase_table\x18\x04 \x01(\x0b\x32-.semantic_model_generator.FullyQualifiedTable\x12\x37\n\x07\x63olumns\x18\x05 \x03(\x0b\x32 .semantic_model_generator.ColumnB\x04\x90\x82\x19\x01\x12=\n\ndimensions\x18\t \x03(\x0b\x32#.semantic_model_generator.DimensionB\x04\x90\x82\x19\x01\x12\x46\n\x0ftime_dimensions\x18\n \x03(\x0b\x32\'.semantic_model_generator.TimeDimensionB\x04\x90\x82\x19\x01\x12\x39\n\x08measures\x18\x0b \x03(\x0b\x32!.semantic_model_generator.MeasureB\x04\x90\x82\x19\x01\x12<\n\x07\x66ilters\x18\x08 \x03(\x0b\x32%.semantic_model_generator.NamedFilterB\x04\x90\x82\x19\x01\"\xb2\x01\n\rSemanticModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x04\x90\x82\x19\x01\x12/\n\x06tables\x18\x03 \x03(\x0b\x32\x1f.semantic_model_generator.Table\x12G\n\x10verified_queries\x18\x06 \x03(\x0b\x32\'.semantic_model_generator.VerifiedQueryB\x04\x90\x82\x19\x01\"\x9f\x02\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x08synonyms\x18\x02 \x03(\tB\x04\x90\x82\x19\x01\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\x90\x82\x19\x01\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\t\x12\x32\n\x04kind\x18\x06 \x01(\x0e\x32$.semantic_model_generator.ColumnKind\x12\x14\n\x06unique\x18\x07 \x01(\x08\x42\x04\x90\x82\x19\x01\x12L\n\x13\x64\x65\x66\x61ult_aggregation\x18\x08 \x01(\x0e\x32).semantic_model_generator.AggregationTypeB\x04\x90\x82\x19\x01\x12\x1b\n\rsample_values\x18\t \x03(\tB\x04\x90\x82\x19\x01\"\x9b\x01\n\rVerifiedQuery\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\x90\x82\x19\x01\x12!\n\x13semantic_model_name\x18\x02 \x01(\tB\x04\x90\x82\x19\x01\x12\x10\n\x08question\x18\x03 \x01(\t\x12\x0b\n\x03sql\x18\x04 \x01(\t\x12\x19\n\x0bverified_at\x18\x05 \x01(\x03\x42\x04\x90\x82\x19\x01\x12\x19\n\x0bverified_by\x18\x06 \x01(\tB\x04\x90\x82\x19\x01*~\n\x0f\x41ggregationType\x12\x1c\n\x18\x61ggregation_type_unknown\x10\x00\x12\x07\n\x03sum\x10\x01\x12\x07\n\x03\x61vg\x10\x02\x12\n\n\x06median\x10\x07\x12\x07\n\x03min\x10\x03\x12\x07\n\x03max\x10\x04\x12\t\n\x05\x63ount\x10\x05\x12\x12\n\x0e\x63ount_distinct\x10\x06*U\n\nColumnKind\x12\x17\n\x13\x63olumn_kind_unknown\x10\x00\x12\r\n\tdimension\x10\x01\x12\x0b\n\x07measure\x10\x02\x12\x12\n\x0etime_dimension\x10\x03:4\n\x08optional\x12\x1d.google.protobuf.FieldOptions\x18\xa2\x90\x03 \x01(\x08\x88\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'semantic_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DIMENSION'].fields_by_name['synonyms']._loaded_options = None
  _globals['_DIMENSION'].fields_by_name['synonyms']._serialized_options = b'\220\202\031\001'
  _globals['_DIMENSION'].fields_by_name['description']._loaded_options = None
  _globals['_DIMENSION'].fields_by_name['description']._serialized_options = b'\220\202\031\001'
  _globals['_DIMENSION'].fields_by_name['unique']._loaded_options = None
  _globals['_DIMENSION'].fields_by_name['unique']._serialized_options = b'\220\202\031\001'
  _globals['_DIMENSION'].fields_by_name['sample_values']._loaded_options = None
  _globals['_DIMENSION'].fields_by_name['sample_values']._serialized_options = b'\220\202\031\001'
  _globals['_TIMEDIMENSION'].fields_by_name['synonyms']._loaded_options = None
  _globals['_TIMEDIMENSION'].fields_by_name['synonyms']._serialized_options = b'\220\202\031\001'
  _globals['_TIMEDIMENSION'].fields_by_name['description']._loaded_options = None
  _globals['_TIMEDIMENSION'].fields_by_name['description']._serialized_options = b'\220\202\031\001'
  _globals['_TIMEDIMENSION'].fields_by_name['unique']._loaded_options = None
  _globals['_TIMEDIMENSION'].fields_by_name['unique']._serialized_options = b'\220\202\031\001'
  _globals['_TIMEDIMENSION'].fields_by_name['sample_values']._loaded_options = None
  _globals['_TIMEDIMENSION'].fields_by_name['sample_values']._serialized_options = b'\220\202\031\001'
  _globals['_MEASURE'].fields_by_name['synonyms']._loaded_options = None
  _globals['_MEASURE'].fields_by_name['synonyms']._serialized_options = b'\220\202\031\001'
  _globals['_MEASURE'].fields_by_name['description']._loaded_options = None
  _globals['_MEASURE'].fields_by_name['description']._serialized_options = b'\220\202\031\001'
  _globals['_MEASURE'].fields_by_name['default_aggregation']._loaded_options = None
  _globals['_MEASURE'].fields_by_name['default_aggregation']._serialized_options = b'\220\202\031\001'
  _globals['_MEASURE'].fields_by_name['sample_values']._loaded_options = None
  _globals['_MEASURE'].fields_by_name['sample_values']._serialized_options = b'\220\202\031\001'
  _globals['_NAMEDFILTER'].fields_by_name['synonyms']._loaded_options = None
  _globals['_NAMEDFILTER'].fields_by_name['synonyms']._serialized_options = b'\220\202\031\001'
  _globals['_NAMEDFILTER'].fields_by_name['description']._loaded_options = None
  _globals['_NAMEDFILTER'].fields_by_name['description']._serialized_options = b'\220\202\031\001'
  _globals['_TABLE'].fields_by_name['synonyms']._loaded_options = None
  _globals['_TABLE'].fields_by_name['synonyms']._serialized_options = b'\220\202\031\001'
  _globals['_TABLE'].fields_by_name['description']._loaded_options = None
  _globals['_TABLE'].fields_by_name['description']._serialized_options = b'\220\202\031\001'
  _globals['_TABLE'].fields_by_name['columns']._loaded_options = None
  _globals['_TABLE'].fields_by_name['columns']._serialized_options = b'\220\202\031\001'
  _globals['_TABLE'].fields_by_name['dimensions']._loaded_options = None
  _globals['_TABLE'].fields_by_name['dimensions']._serialized_options = b'\220\202\031\001'
  _globals['_TABLE'].fields_by_name['time_dimensions']._loaded_options = None
  _globals['_TABLE'].fields_by_name['time_dimensions']._serialized_options = b'\220\202\031\001'
  _globals['_TABLE'].fields_by_name['measures']._loaded_options = None
  _globals['_TABLE'].fields_by_name['measures']._serialized_options = b'\220\202\031\001'
  _globals['_TABLE'].fields_by_name['filters']._loaded_options = None
  _globals['_TABLE'].fields_by_name['filters']._serialized_options = b'\220\202\031\001'
  _globals['_SEMANTICMODEL'].fields_by_name['description']._loaded_options = None
  _globals['_SEMANTICMODEL'].fields_by_name['description']._serialized_options = b'\220\202\031\001'
  _globals['_SEMANTICMODEL'].fields_by_name['verified_queries']._loaded_options = None
  _globals['_SEMANTICMODEL'].fields_by_name['verified_queries']._serialized_options = b'\220\202\031\001'
  _globals['_COLUMN'].fields_by_name['synonyms']._loaded_options = None
  _globals['_COLUMN'].fields_by_name['synonyms']._serialized_options = b'\220\202\031\001'
  _globals['_COLUMN'].fields_by_name['description']._loaded_options = None
  _globals['_COLUMN'].fields_by_name['description']._serialized_options = b'\220\202\031\001'
  _globals['_COLUMN'].fields_by_name['unique']._loaded_options = None
  _globals['_COLUMN'].fields_by_name['unique']._serialized_options = b'\220\202\031\001'
  _globals['_COLUMN'].fields_by_name['default_aggregation']._loaded_options = None
  _globals['_COLUMN'].fields_by_name['default_aggregation']._serialized_options = b'\220\202\031\001'
  _globals['_COLUMN'].fields_by_name['sample_values']._loaded_options = None
  _globals['_COLUMN'].fields_by_name['sample_values']._serialized_options = b'\220\202\031\001'
  _globals['_VERIFIEDQUERY'].fields_by_name['name']._loaded_options = None
  _globals['_VERIFIEDQUERY'].fields_by_name['name']._serialized_options = b'\220\202\031\001'
  _globals['_VERIFIEDQUERY'].fields_by_name['semantic_model_name']._loaded_options = None
  _globals['_VERIFIEDQUERY'].fields_by_name['semantic_model_name']._serialized_options = b'\220\202\031\001'
  _globals['_VERIFIEDQUERY'].fields_by_name['verified_at']._loaded_options = None
  _globals['_VERIFIEDQUERY'].fields_by_name['verified_at']._serialized_options = b'\220\202\031\001'
  _globals['_VERIFIEDQUERY'].fields_by_name['verified_by']._loaded_options = None
  _globals['_VERIFIEDQUERY'].fields_by_name['verified_by']._serialized_options = b'\220\202\031\001'
  _globals['_AGGREGATIONTYPE']._serialized_start=1881
  _globals['_AGGREGATIONTYPE']._serialized_end=2007
  _globals['_COLUMNKIND']._serialized_start=2009
  _globals['_COLUMNKIND']._serialized_end=2094
  _globals['_DIMENSION']._serialized_start=85
  _globals['_DIMENSION']._serialized_end=245
  _globals['_TIMEDIMENSION']._serialized_start=248
  _globals['_TIMEDIMENSION']._serialized_end=412
  _globals['_MEASURE']._serialized_start=415
  _globals['_MEASURE']._serialized_end=629
  _globals['_NAMEDFILTER']._serialized_start=631
  _globals['_NAMEDFILTER']._serialized_end=723
  _globals['_FULLYQUALIFIEDTABLE']._serialized_start=725
  _globals['_FULLYQUALIFIEDTABLE']._serialized_end=795
  _globals['_TABLE']._serialized_start=798
  _globals['_TABLE']._serialized_end=1250
  _globals['_SEMANTICMODEL']._serialized_start=1253
  _globals['_SEMANTICMODEL']._serialized_end=1431
  _globals['_COLUMN']._serialized_start=1434
  _globals['_COLUMN']._serialized_end=1721
  _globals['_VERIFIEDQUERY']._serialized_start=1724
  _globals['_VERIFIEDQUERY']._serialized_end=1879
# @@protoc_insertion_point(module_scope)
