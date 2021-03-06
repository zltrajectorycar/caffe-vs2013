# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caffe_pretty_print.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import caffe_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='caffe_pretty_print.proto',
  package='caffe',
  serialized_pb='\n\x18\x63\x61\x66\x66\x65_pretty_print.proto\x12\x05\x63\x61\x66\x66\x65\x1a\x0b\x63\x61\x66\x66\x65.proto\"\x8f\x01\n\x17NetParameterPrettyPrint\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x0e\x66orce_backward\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\r\n\x05input\x18\x03 \x03(\t\x12\x11\n\tinput_dim\x18\x04 \x03(\x05\x12%\n\x06layers\x18\x05 \x03(\x0b\x32\x15.caffe.LayerParameter')




_NETPARAMETERPRETTYPRINT = _descriptor.Descriptor(
  name='NetParameterPrettyPrint',
  full_name='caffe.NetParameterPrettyPrint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='caffe.NetParameterPrettyPrint.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='force_backward', full_name='caffe.NetParameterPrettyPrint.force_backward', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input', full_name='caffe.NetParameterPrettyPrint.input', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_dim', full_name='caffe.NetParameterPrettyPrint.input_dim', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layers', full_name='caffe.NetParameterPrettyPrint.layers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=49,
  serialized_end=192,
)

_NETPARAMETERPRETTYPRINT.fields_by_name['layers'].message_type = caffe_pb2._LAYERPARAMETER
DESCRIPTOR.message_types_by_name['NetParameterPrettyPrint'] = _NETPARAMETERPRETTYPRINT

class NetParameterPrettyPrint(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NETPARAMETERPRETTYPRINT

  # @@protoc_insertion_point(class_scope:caffe.NetParameterPrettyPrint)


# @@protoc_insertion_point(module_scope)
