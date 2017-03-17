import tensorflow as tf

state = tf.Variable(0, name="test")
one = tf.constant(1)

new_value = tf.add(state, one)

updata = state.assign(new_value)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(4):
        sess.run(updata)
        print(sess.run(state))
