# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tagdeterminer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13tagdeterminer.proto\x12\rtagdeterminer\"\x0e\n\x0c\x41\x62outRequest\"+\n\nAboutReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07tag_cls\x18\x02 \x01(\t\"9\n\x14\x44\x65termineTagsRequest\x12\x10\n\x08mimetype\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"!\n\x12\x44\x65termineTagsReply\x12\x0b\n\x03tag\x18\x01 \x03(\t2\xaf\x01\n\rTagDeterminer\x12\x41\n\x05\x41\x62out\x12\x1b.tagdeterminer.AboutRequest\x1a\x19.tagdeterminer.AboutReply\"\x00\x12[\n\rDetermineTags\x12#.tagdeterminer.DetermineTagsRequest\x1a!.tagdeterminer.DetermineTagsReply\"\x00(\x01\x42:\n$com.vaguehope.dlnatoad.tagdeterminerB\x12TagDeterminerProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tagdeterminer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.vaguehope.dlnatoad.tagdeterminerB\022TagDeterminerProto'
  _globals['_ABOUTREQUEST']._serialized_start=38
  _globals['_ABOUTREQUEST']._serialized_end=52
  _globals['_ABOUTREPLY']._serialized_start=54
  _globals['_ABOUTREPLY']._serialized_end=97
  _globals['_DETERMINETAGSREQUEST']._serialized_start=99
  _globals['_DETERMINETAGSREQUEST']._serialized_end=156
  _globals['_DETERMINETAGSREPLY']._serialized_start=158
  _globals['_DETERMINETAGSREPLY']._serialized_end=191
  _globals['_TAGDETERMINER']._serialized_start=194
  _globals['_TAGDETERMINER']._serialized_end=369
# @@protoc_insertion_point(module_scope)
