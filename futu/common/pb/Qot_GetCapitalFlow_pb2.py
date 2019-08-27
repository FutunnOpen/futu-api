# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_GetCapitalFlow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_GetCapitalFlow.proto',
  package='Qot_GetCapitalFlow',
  syntax='proto2',
  serialized_pb=_b('\n\x18Qot_GetCapitalFlow.proto\x12\x12Qot_GetCapitalFlow\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"-\n\x03\x43\x32S\x12&\n\x08security\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\"B\n\x0f\x43\x61pitalFlowItem\x12\x0e\n\x06inFlow\x18\x01 \x02(\x01\x12\x0c\n\x04time\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\"s\n\x03S2C\x12\x39\n\x0c\x66lowItemList\x18\x01 \x03(\x0b\x32#.Qot_GetCapitalFlow.CapitalFlowItem\x12\x15\n\rlastValidTime\x18\x02 \x01(\t\x12\x1a\n\x12lastValidTimestamp\x18\x03 \x01(\x01\"/\n\x07Request\x12$\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x17.Qot_GetCapitalFlow.C2S\"h\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12$\n\x03s2c\x18\x04 \x01(\x0b\x32\x17.Qot_GetCapitalFlow.S2CB\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_GetCapitalFlow.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_GetCapitalFlow.C2S.security', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=125,
)


_CAPITALFLOWITEM = _descriptor.Descriptor(
  name='CapitalFlowItem',
  full_name='Qot_GetCapitalFlow.CapitalFlowItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inFlow', full_name='Qot_GetCapitalFlow.CapitalFlowItem.inFlow', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='Qot_GetCapitalFlow.CapitalFlowItem.time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Qot_GetCapitalFlow.CapitalFlowItem.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=193,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_GetCapitalFlow.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flowItemList', full_name='Qot_GetCapitalFlow.S2C.flowItemList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastValidTime', full_name='Qot_GetCapitalFlow.S2C.lastValidTime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastValidTimestamp', full_name='Qot_GetCapitalFlow.S2C.lastValidTimestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=310,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_GetCapitalFlow.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_GetCapitalFlow.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=359,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_GetCapitalFlow.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_GetCapitalFlow.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_GetCapitalFlow.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_GetCapitalFlow.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_GetCapitalFlow.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=465,
)

_C2S.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_S2C.fields_by_name['flowItemList'].message_type = _CAPITALFLOWITEM
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['CapitalFlowItem'] = _CAPITALFLOWITEM
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_GetCapitalFlow_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalFlow.C2S)
  ))
_sym_db.RegisterMessage(C2S)

CapitalFlowItem = _reflection.GeneratedProtocolMessageType('CapitalFlowItem', (_message.Message,), dict(
  DESCRIPTOR = _CAPITALFLOWITEM,
  __module__ = 'Qot_GetCapitalFlow_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalFlow.CapitalFlowItem)
  ))
_sym_db.RegisterMessage(CapitalFlowItem)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_GetCapitalFlow_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalFlow.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_GetCapitalFlow_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalFlow.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_GetCapitalFlow_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalFlow.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)
