import tensorflow as tf
import matplotlib.pyplot as plt
normal = tf.random_normal([3, 3], 5, 1, name="normal")

with tf.Session() as sess:
    print(normal.name)
    print(sess.run(normal))





