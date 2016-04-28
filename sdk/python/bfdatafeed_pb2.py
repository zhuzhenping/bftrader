# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bfdatafeed.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bftrader_pb2 as bftrader__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bfdatafeed.proto',
  package='bftrader.bfdatafeed',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x62\x66\x64\x61tafeed.proto\x12\x13\x62\x66trader.bfdatafeed\x1a\x0e\x62\x66trader.proto2\x84\x05\n\x11\x42\x66\x44\x61tafeedService\x12\x34\n\x04Ping\x12\x14.bftrader.BfPingData\x1a\x14.bftrader.BfPingData\"\x00\x12\x36\n\nInsertTick\x12\x14.bftrader.BfTickData\x1a\x10.bftrader.BfVoid\"\x00\x12;\n\x07GetTick\x12\x16.bftrader.BfGetTickReq\x1a\x14.bftrader.BfTickData\"\x00\x30\x01\x12;\n\nDeleteTick\x12\x19.bftrader.BfDeleteTickReq\x1a\x10.bftrader.BfVoid\"\x00\x12\x34\n\tInsertBar\x12\x13.bftrader.BfBarData\x1a\x10.bftrader.BfVoid\"\x00\x12\x38\n\x06GetBar\x12\x15.bftrader.BfGetBarReq\x1a\x13.bftrader.BfBarData\"\x00\x30\x01\x12\x39\n\tDeleteBar\x12\x18.bftrader.BfDeleteBarReq\x1a\x10.bftrader.BfVoid\"\x00\x12>\n\x0eInsertContract\x12\x18.bftrader.BfContractData\x1a\x10.bftrader.BfVoid\"\x00\x12O\n\x0bGetContract\x12\".bftrader.BfDatafeedGetContractReq\x1a\x18.bftrader.BfContractData\"\x00\x30\x01\x12K\n\x0e\x44\x65leteContract\x12%.bftrader.BfDatafeedDeleteContractReq\x1a\x10.bftrader.BfVoid\"\x00\x42\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bftrader__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaBfDatafeedServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InsertTick(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetTick(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteTick(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InsertBar(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetBar(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteBar(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InsertContract(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetContract(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteContract(self, request, context):
    raise NotImplementedError()

class BetaBfDatafeedServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request, timeout):
    raise NotImplementedError()
  Ping.future = None
  @abc.abstractmethod
  def InsertTick(self, request, timeout):
    raise NotImplementedError()
  InsertTick.future = None
  @abc.abstractmethod
  def GetTick(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteTick(self, request, timeout):
    raise NotImplementedError()
  DeleteTick.future = None
  @abc.abstractmethod
  def InsertBar(self, request, timeout):
    raise NotImplementedError()
  InsertBar.future = None
  @abc.abstractmethod
  def GetBar(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteBar(self, request, timeout):
    raise NotImplementedError()
  DeleteBar.future = None
  @abc.abstractmethod
  def InsertContract(self, request, timeout):
    raise NotImplementedError()
  InsertContract.future = None
  @abc.abstractmethod
  def GetContract(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteContract(self, request, timeout):
    raise NotImplementedError()
  DeleteContract.future = None

def beta_create_BfDatafeedService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  request_deserializers = {
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteBar'): bftrader_pb2.BfDeleteBarReq.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteContract'): bftrader_pb2.BfDatafeedDeleteContractReq.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteTick'): bftrader_pb2.BfDeleteTickReq.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetBar'): bftrader_pb2.BfGetBarReq.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetContract'): bftrader_pb2.BfDatafeedGetContractReq.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetTick'): bftrader_pb2.BfGetTickReq.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertBar'): bftrader_pb2.BfBarData.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertContract'): bftrader_pb2.BfContractData.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertTick'): bftrader_pb2.BfTickData.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'Ping'): bftrader_pb2.BfPingData.FromString,
  }
  response_serializers = {
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteBar'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteContract'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteTick'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetBar'): bftrader_pb2.BfBarData.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetContract'): bftrader_pb2.BfContractData.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetTick'): bftrader_pb2.BfTickData.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertBar'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertContract'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertTick'): bftrader_pb2.BfVoid.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'Ping'): bftrader_pb2.BfPingData.SerializeToString,
  }
  method_implementations = {
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteBar'): face_utilities.unary_unary_inline(servicer.DeleteBar),
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteContract'): face_utilities.unary_unary_inline(servicer.DeleteContract),
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteTick'): face_utilities.unary_unary_inline(servicer.DeleteTick),
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetBar'): face_utilities.unary_stream_inline(servicer.GetBar),
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetContract'): face_utilities.unary_stream_inline(servicer.GetContract),
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetTick'): face_utilities.unary_stream_inline(servicer.GetTick),
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertBar'): face_utilities.unary_unary_inline(servicer.InsertBar),
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertContract'): face_utilities.unary_unary_inline(servicer.InsertContract),
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertTick'): face_utilities.unary_unary_inline(servicer.InsertTick),
    ('bftrader.bfdatafeed.BfDatafeedService', 'Ping'): face_utilities.unary_unary_inline(servicer.Ping),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_BfDatafeedService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  import bftrader_pb2
  request_serializers = {
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteBar'): bftrader_pb2.BfDeleteBarReq.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteContract'): bftrader_pb2.BfDatafeedDeleteContractReq.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteTick'): bftrader_pb2.BfDeleteTickReq.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetBar'): bftrader_pb2.BfGetBarReq.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetContract'): bftrader_pb2.BfDatafeedGetContractReq.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetTick'): bftrader_pb2.BfGetTickReq.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertBar'): bftrader_pb2.BfBarData.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertContract'): bftrader_pb2.BfContractData.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertTick'): bftrader_pb2.BfTickData.SerializeToString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'Ping'): bftrader_pb2.BfPingData.SerializeToString,
  }
  response_deserializers = {
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteBar'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteContract'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'DeleteTick'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetBar'): bftrader_pb2.BfBarData.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetContract'): bftrader_pb2.BfContractData.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'GetTick'): bftrader_pb2.BfTickData.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertBar'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertContract'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'InsertTick'): bftrader_pb2.BfVoid.FromString,
    ('bftrader.bfdatafeed.BfDatafeedService', 'Ping'): bftrader_pb2.BfPingData.FromString,
  }
  cardinalities = {
    'DeleteBar': cardinality.Cardinality.UNARY_UNARY,
    'DeleteContract': cardinality.Cardinality.UNARY_UNARY,
    'DeleteTick': cardinality.Cardinality.UNARY_UNARY,
    'GetBar': cardinality.Cardinality.UNARY_STREAM,
    'GetContract': cardinality.Cardinality.UNARY_STREAM,
    'GetTick': cardinality.Cardinality.UNARY_STREAM,
    'InsertBar': cardinality.Cardinality.UNARY_UNARY,
    'InsertContract': cardinality.Cardinality.UNARY_UNARY,
    'InsertTick': cardinality.Cardinality.UNARY_UNARY,
    'Ping': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'bftrader.bfdatafeed.BfDatafeedService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
