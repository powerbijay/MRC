
import numpy as np
import tensorflow as tf

cc = tf.ones([5,5,100,100])
dd = tf.ones([100,100])
init=tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(cc*dd).shape)

# sim_matrix  [batch, p_l, q_l]
# p_encode  [batch, p_l, 2D]
# q_encode  [batch, q_l, 2D]
# w  [2D, 2D]

