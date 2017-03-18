import tensorflow as tf

zeros = tf.zeros([2, 2], name="zeros")
ones = tf.ones([3, 3], name="ones")

tensor = ([[1, 2, 3],
           [4, 5, 6]])
zlike = tf.zeros_like(tensor, name="zlike")
olike = tf.ones_like(tensor, name="olike")

fill = tf.fill([1, 2], 3, "fill")


with tf.Session() as sess:
    print(zeros.name)
    print(sess.run(zeros))
    print(ones.name)
    print(sess.run(ones))
    print(zlike.name)
    print(sess.run(zlike))
    print(olike.name)
    print(sess.run(olike))
    print(fill.name)
    print(sess.run(fill))