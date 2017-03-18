# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main/resources/chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='main/resources/chat.proto',
  package='com.talent.aio.examples.im.common.packets',
  syntax='proto3',
  serialized_pb=_b('\n\x19main/resources/chat.proto\x12)com.talent.aio.examples.im.common.packets\"\xd7\x01\n\x0b\x41uthReqBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x10\n\x08\x64\x65viceId\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\x12I\n\ndeviceType\x18\x04 \x01(\x0e\x32\x35.com.talent.aio.examples.im.common.packets.DeviceType\x12\x0b\n\x03\x63id\x18\x05 \x01(\t\x12\x12\n\nappVersion\x18\x06 \x01(\t\x12\x12\n\ndeviceInfo\x18\x07 \x01(\t\x12\x0b\n\x03seq\x18\x08 \x01(\x03\x12\x0c\n\x04sign\x18\t \x01(\t\"\x1c\n\x0c\x41uthRespBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\"*\n\x0bJoinReqBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\r\n\x05group\x18\x02 \x01(\t\"w\n\x0cJoinRespBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12J\n\x06result\x18\x02 \x01(\x0e\x32:.com.talent.aio.examples.im.common.packets.JoinGroupResult\x12\r\n\x05group\x18\x03 \x01(\t\"\x99\x01\n\x0b\x43hatReqBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32\x33.com.talent.aio.examples.im.common.packets.ChatType\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\r\n\x05group\x18\x04 \x01(\t\x12\x0c\n\x04toId\x18\x05 \x01(\x05\x12\x0e\n\x06toNick\x18\x06 \x01(\t\"\xbc\x01\n\x0c\x43hatRespBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32\x33.com.talent.aio.examples.im.common.packets.ChatType\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0e\n\x06\x66romId\x18\x04 \x01(\x05\x12\x10\n\x08\x66romNick\x18\x05 \x01(\t\x12\x0c\n\x04toId\x18\x06 \x01(\x05\x12\x0e\n\x06toNick\x18\x07 \x01(\t\x12\r\n\x05group\x18\x08 \x01(\t\"\"\n\x12\x42\x65ginToLiveReqBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\"`\n\x13\x42\x65ginToLiveRespBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0e\n\x06liveid\x18\x02 \x01(\x03\x12\x16\n\x0ertmppublishurl\x18\x03 \x01(\t\x12\x13\n\x0brtmpliveurl\x18\x04 \x01(\t\"\x1e\n\x0e\x45ndLiveReqBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\"/\n\x0f\x45ndLiveRespBody\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0e\n\x06liveid\x18\x02 \x01(\x03*f\n\nDeviceType\x12\x16\n\x12\x44\x45VICE_TYPE_UNKNOW\x10\x00\x12\x12\n\x0e\x44\x45VICE_TYPE_PC\x10\x01\x12\x17\n\x13\x44\x45VICE_TYPE_ANDROID\x10\x02\x12\x13\n\x0f\x44\x45VICE_TYPE_IOS\x10\x03*\xb2\x03\n\x07\x43ommand\x12\x12\n\x0e\x43OMMAND_UNKNOW\x10\x00\x12\x19\n\x15\x43OMMAND_HANDSHAKE_REQ\x10\x01\x12\x1a\n\x16\x43OMMAND_HANDSHAKE_RESP\x10\x02\x12\x14\n\x10\x43OMMAND_AUTH_REQ\x10\x03\x12\x15\n\x11\x43OMMAND_AUTH_RESP\x10\x04\x12\x1a\n\x16\x43OMMAND_JOIN_GROUP_REQ\x10\x05\x12\x1b\n\x17\x43OMMAND_JOIN_GROUP_RESP\x10\x06\x12\"\n\x1e\x43OMMAND_JOIN_GROUP_NOTIFY_RESP\x10\x07\x12\x14\n\x10\x43OMMAND_CHAT_REQ\x10\x08\x12\x15\n\x11\x43OMMAND_CHAT_RESP\x10\t\x12\x1a\n\x16\x43OMMAND_START_SHOW_REQ\x10\n\x12\x1b\n\x17\x43OMMAND_START_SHOW_RESP\x10\x0b\x12\x18\n\x14\x43OMMAND_END_SHOW_REQ\x10\x0c\x12 \n\x1c\x43OMMAND_END_SHOW_NOTIFY_RESP\x10\r\x12\x19\n\x15\x43OMMAND_HEARTBEAT_REQ\x10\x0e\x12\x15\n\x11\x43OMMAND_CLOSE_REQ\x10\x0f*\xd0\x01\n\x0fJoinGroupResult\x12\x1c\n\x18JOIN_GROUP_RESULT_UNKNOW\x10\x00\x12\x18\n\x14JOIN_GROUP_RESULT_OK\x10\x01\x12\x1f\n\x1bJOIN_GROUP_RESULT_NOT_EXIST\x10\x02\x12 \n\x1cJOIN_GROUP_RESULT_GROUP_FULL\x10\x03\x12!\n\x1dJOIN_GROUP_RESULT_IN_BACKLIST\x10\x04\x12\x1f\n\x1bJOIN_GROUP_RESULT_TAKEOUTED\x10\x05*M\n\x08\x43hatType\x12\x14\n\x10\x43HAT_TYPE_UNKNOW\x10\x00\x12\x14\n\x10\x43HAT_TYPE_PUBLIC\x10\x01\x12\x15\n\x11\x43HAT_TYPE_PRIVATE\x10\x02\x42-\n)com.talent.aio.examples.im.common.packetsP\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='com.talent.aio.examples.im.common.packets.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TYPE_UNKNOW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TYPE_PC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TYPE_ANDROID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TYPE_IOS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1047,
  serialized_end=1149,
)
_sym_db.RegisterEnumDescriptor(_DEVICETYPE)

DeviceType = enum_type_wrapper.EnumTypeWrapper(_DEVICETYPE)
_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='com.talent.aio.examples.im.common.packets.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMMAND_UNKNOW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_HANDSHAKE_REQ', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_HANDSHAKE_RESP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_AUTH_REQ', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_AUTH_RESP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_JOIN_GROUP_REQ', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_JOIN_GROUP_RESP', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_JOIN_GROUP_NOTIFY_RESP', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_CHAT_REQ', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_CHAT_RESP', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_START_SHOW_REQ', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_START_SHOW_RESP', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_END_SHOW_REQ', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_END_SHOW_NOTIFY_RESP', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_HEARTBEAT_REQ', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_CLOSE_REQ', index=15, number=15,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1152,
  serialized_end=1586,
)
_sym_db.RegisterEnumDescriptor(_COMMAND)

Command = enum_type_wrapper.EnumTypeWrapper(_COMMAND)
_JOINGROUPRESULT = _descriptor.EnumDescriptor(
  name='JoinGroupResult',
  full_name='com.talent.aio.examples.im.common.packets.JoinGroupResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOIN_GROUP_RESULT_UNKNOW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN_GROUP_RESULT_OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN_GROUP_RESULT_NOT_EXIST', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN_GROUP_RESULT_GROUP_FULL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN_GROUP_RESULT_IN_BACKLIST', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN_GROUP_RESULT_TAKEOUTED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1589,
  serialized_end=1797,
)
_sym_db.RegisterEnumDescriptor(_JOINGROUPRESULT)

JoinGroupResult = enum_type_wrapper.EnumTypeWrapper(_JOINGROUPRESULT)
_CHATTYPE = _descriptor.EnumDescriptor(
  name='ChatType',
  full_name='com.talent.aio.examples.im.common.packets.ChatType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHAT_TYPE_UNKNOW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAT_TYPE_PUBLIC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAT_TYPE_PRIVATE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1799,
  serialized_end=1876,
)
_sym_db.RegisterEnumDescriptor(_CHATTYPE)

ChatType = enum_type_wrapper.EnumTypeWrapper(_CHATTYPE)
DEVICE_TYPE_UNKNOW = 0
DEVICE_TYPE_PC = 1
DEVICE_TYPE_ANDROID = 2
DEVICE_TYPE_IOS = 3
COMMAND_UNKNOW = 0
COMMAND_HANDSHAKE_REQ = 1
COMMAND_HANDSHAKE_RESP = 2
COMMAND_AUTH_REQ = 3
COMMAND_AUTH_RESP = 4
COMMAND_JOIN_GROUP_REQ = 5
COMMAND_JOIN_GROUP_RESP = 6
COMMAND_JOIN_GROUP_NOTIFY_RESP = 7
COMMAND_CHAT_REQ = 8
COMMAND_CHAT_RESP = 9
COMMAND_START_SHOW_REQ = 10
COMMAND_START_SHOW_RESP = 11
COMMAND_END_SHOW_REQ = 12
COMMAND_END_SHOW_NOTIFY_RESP = 13
COMMAND_HEARTBEAT_REQ = 14
COMMAND_CLOSE_REQ = 15
JOIN_GROUP_RESULT_UNKNOW = 0
JOIN_GROUP_RESULT_OK = 1
JOIN_GROUP_RESULT_NOT_EXIST = 2
JOIN_GROUP_RESULT_GROUP_FULL = 3
JOIN_GROUP_RESULT_IN_BACKLIST = 4
JOIN_GROUP_RESULT_TAKEOUTED = 5
CHAT_TYPE_UNKNOW = 0
CHAT_TYPE_PUBLIC = 1
CHAT_TYPE_PRIVATE = 2



_AUTHREQBODY = _descriptor.Descriptor(
  name='AuthReqBody',
  full_name='com.talent.aio.examples.im.common.packets.AuthReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.deviceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceType', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.deviceType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cid', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.cid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appVersion', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.appVersion', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceInfo', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.deviceInfo', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.seq', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sign', full_name='com.talent.aio.examples.im.common.packets.AuthReqBody.sign', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=288,
)


_AUTHRESPBODY = _descriptor.Descriptor(
  name='AuthRespBody',
  full_name='com.talent.aio.examples.im.common.packets.AuthRespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.AuthRespBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=318,
)


_JOINREQBODY = _descriptor.Descriptor(
  name='JoinReqBody',
  full_name='com.talent.aio.examples.im.common.packets.JoinReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.JoinReqBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='com.talent.aio.examples.im.common.packets.JoinReqBody.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=362,
)


_JOINRESPBODY = _descriptor.Descriptor(
  name='JoinRespBody',
  full_name='com.talent.aio.examples.im.common.packets.JoinRespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.JoinRespBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='com.talent.aio.examples.im.common.packets.JoinRespBody.result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='com.talent.aio.examples.im.common.packets.JoinRespBody.group', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=483,
)


_CHATREQBODY = _descriptor.Descriptor(
  name='ChatReqBody',
  full_name='com.talent.aio.examples.im.common.packets.ChatReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.ChatReqBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.talent.aio.examples.im.common.packets.ChatReqBody.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='com.talent.aio.examples.im.common.packets.ChatReqBody.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='com.talent.aio.examples.im.common.packets.ChatReqBody.group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toId', full_name='com.talent.aio.examples.im.common.packets.ChatReqBody.toId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toNick', full_name='com.talent.aio.examples.im.common.packets.ChatReqBody.toNick', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=639,
)


_CHATRESPBODY = _descriptor.Descriptor(
  name='ChatRespBody',
  full_name='com.talent.aio.examples.im.common.packets.ChatRespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromId', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.fromId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromNick', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.fromNick', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toId', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.toId', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toNick', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.toNick', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='com.talent.aio.examples.im.common.packets.ChatRespBody.group', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=642,
  serialized_end=830,
)


_BEGINTOLIVEREQBODY = _descriptor.Descriptor(
  name='BeginToLiveReqBody',
  full_name='com.talent.aio.examples.im.common.packets.BeginToLiveReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.BeginToLiveReqBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=832,
  serialized_end=866,
)


_BEGINTOLIVERESPBODY = _descriptor.Descriptor(
  name='BeginToLiveRespBody',
  full_name='com.talent.aio.examples.im.common.packets.BeginToLiveRespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.BeginToLiveRespBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='liveid', full_name='com.talent.aio.examples.im.common.packets.BeginToLiveRespBody.liveid', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtmppublishurl', full_name='com.talent.aio.examples.im.common.packets.BeginToLiveRespBody.rtmppublishurl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtmpliveurl', full_name='com.talent.aio.examples.im.common.packets.BeginToLiveRespBody.rtmpliveurl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=868,
  serialized_end=964,
)


_ENDLIVEREQBODY = _descriptor.Descriptor(
  name='EndLiveReqBody',
  full_name='com.talent.aio.examples.im.common.packets.EndLiveReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.EndLiveReqBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=966,
  serialized_end=996,
)


_ENDLIVERESPBODY = _descriptor.Descriptor(
  name='EndLiveRespBody',
  full_name='com.talent.aio.examples.im.common.packets.EndLiveRespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.talent.aio.examples.im.common.packets.EndLiveRespBody.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='liveid', full_name='com.talent.aio.examples.im.common.packets.EndLiveRespBody.liveid', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=998,
  serialized_end=1045,
)

_AUTHREQBODY.fields_by_name['deviceType'].enum_type = _DEVICETYPE
_JOINRESPBODY.fields_by_name['result'].enum_type = _JOINGROUPRESULT
_CHATREQBODY.fields_by_name['type'].enum_type = _CHATTYPE
_CHATRESPBODY.fields_by_name['type'].enum_type = _CHATTYPE
DESCRIPTOR.message_types_by_name['AuthReqBody'] = _AUTHREQBODY
DESCRIPTOR.message_types_by_name['AuthRespBody'] = _AUTHRESPBODY
DESCRIPTOR.message_types_by_name['JoinReqBody'] = _JOINREQBODY
DESCRIPTOR.message_types_by_name['JoinRespBody'] = _JOINRESPBODY
DESCRIPTOR.message_types_by_name['ChatReqBody'] = _CHATREQBODY
DESCRIPTOR.message_types_by_name['ChatRespBody'] = _CHATRESPBODY
DESCRIPTOR.message_types_by_name['BeginToLiveReqBody'] = _BEGINTOLIVEREQBODY
DESCRIPTOR.message_types_by_name['BeginToLiveRespBody'] = _BEGINTOLIVERESPBODY
DESCRIPTOR.message_types_by_name['EndLiveReqBody'] = _ENDLIVEREQBODY
DESCRIPTOR.message_types_by_name['EndLiveRespBody'] = _ENDLIVERESPBODY
DESCRIPTOR.enum_types_by_name['DeviceType'] = _DEVICETYPE
DESCRIPTOR.enum_types_by_name['Command'] = _COMMAND
DESCRIPTOR.enum_types_by_name['JoinGroupResult'] = _JOINGROUPRESULT
DESCRIPTOR.enum_types_by_name['ChatType'] = _CHATTYPE

AuthReqBody = _reflection.GeneratedProtocolMessageType('AuthReqBody', (_message.Message,), dict(
  DESCRIPTOR = _AUTHREQBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.AuthReqBody)
  ))
_sym_db.RegisterMessage(AuthReqBody)

AuthRespBody = _reflection.GeneratedProtocolMessageType('AuthRespBody', (_message.Message,), dict(
  DESCRIPTOR = _AUTHRESPBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.AuthRespBody)
  ))
_sym_db.RegisterMessage(AuthRespBody)

JoinReqBody = _reflection.GeneratedProtocolMessageType('JoinReqBody', (_message.Message,), dict(
  DESCRIPTOR = _JOINREQBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.JoinReqBody)
  ))
_sym_db.RegisterMessage(JoinReqBody)

JoinRespBody = _reflection.GeneratedProtocolMessageType('JoinRespBody', (_message.Message,), dict(
  DESCRIPTOR = _JOINRESPBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.JoinRespBody)
  ))
_sym_db.RegisterMessage(JoinRespBody)

ChatReqBody = _reflection.GeneratedProtocolMessageType('ChatReqBody', (_message.Message,), dict(
  DESCRIPTOR = _CHATREQBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.ChatReqBody)
  ))
_sym_db.RegisterMessage(ChatReqBody)

ChatRespBody = _reflection.GeneratedProtocolMessageType('ChatRespBody', (_message.Message,), dict(
  DESCRIPTOR = _CHATRESPBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.ChatRespBody)
  ))
_sym_db.RegisterMessage(ChatRespBody)

BeginToLiveReqBody = _reflection.GeneratedProtocolMessageType('BeginToLiveReqBody', (_message.Message,), dict(
  DESCRIPTOR = _BEGINTOLIVEREQBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.BeginToLiveReqBody)
  ))
_sym_db.RegisterMessage(BeginToLiveReqBody)

BeginToLiveRespBody = _reflection.GeneratedProtocolMessageType('BeginToLiveRespBody', (_message.Message,), dict(
  DESCRIPTOR = _BEGINTOLIVERESPBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.BeginToLiveRespBody)
  ))
_sym_db.RegisterMessage(BeginToLiveRespBody)

EndLiveReqBody = _reflection.GeneratedProtocolMessageType('EndLiveReqBody', (_message.Message,), dict(
  DESCRIPTOR = _ENDLIVEREQBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.EndLiveReqBody)
  ))
_sym_db.RegisterMessage(EndLiveReqBody)

EndLiveRespBody = _reflection.GeneratedProtocolMessageType('EndLiveRespBody', (_message.Message,), dict(
  DESCRIPTOR = _ENDLIVERESPBODY,
  __module__ = 'main.resources.chat_pb2'
  # @@protoc_insertion_point(class_scope:com.talent.aio.examples.im.common.packets.EndLiveRespBody)
  ))
_sym_db.RegisterMessage(EndLiveRespBody)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n)com.talent.aio.examples.im.common.packetsP\001'))
# @@protoc_insertion_point(module_scope)
