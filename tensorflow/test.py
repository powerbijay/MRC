
import numpy as np
import tensorflow as tf


#
# pl = tf.placeholder(tf.int32,[None,None])
#
# cc = pl
# print(cc.get_shape().as_list())
# init=tf.initialize_all_variables()
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(cc,feed_dict={pl:np.ones([2,2])}))
#
# # sim_matrix  [batch, p_l, q_l]
# # p_encode  [batch, p_l, 2D]
# # q_encode  [batch, q_l, 2D]
# # w  [2D, 2D]

list = [2,2,2,2,2,2]
print(list[0:10])

