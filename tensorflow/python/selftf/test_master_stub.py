from __future__ import print_function

import grpc
import master_pb2


class Stub(object):

  def __init__(self, channel):
    """
    :param grpc.Channel channel:
    """

    self.Reconfig = channel.unary_unary(
        '/tensorflow.MasterService/Reconfig',
        request_serializer=master_pb2.ReconfigRequest.SerializeToString,
        response_deserializer=master_pb2.ReconfigResponse.FromString,
    )


def run():
  channel = grpc.insecure_channel('localhost:2222')
  stub = Stub(channel)
  print("-------------- Reconfig --------------")
  stub.Reconfig(master_pb2.ReconfigRequest())

run()
