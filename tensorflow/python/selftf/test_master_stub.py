from __future__ import print_function

import grpc
import master_pb2
import tensorflow as tf


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


  # Create a graph
  a = tf.get_variable("a", [], initializer=tf.constant_initializer(1))
  b = tf.get_variable("b", [], initializer=tf.constant_initializer(3))
  c = tf.add(a,b,"c")

  sv = tf.train.Supervisor()
  # run
  with sv.prepare_or_wait_for_session("grpc://localhost:2222") as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(c))

    # test dynamic
    d = tf.multiply(a,b,"d")
    print(sess.run(d))



  # channel = grpc.insecure_channel('localhost:2222')
  # stub = Stub(channel)
  # print("-------------- Reconfig --------------")
  # stub.Reconfig(master_pb2.ReconfigRequest())

run()
