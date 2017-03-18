import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_fun=None):
    with tf.name_scope('layer'):
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
        Wx_plus_b = tf.matmul(inputs, Weights) + biases

        if activation_fun is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_fun(Wx_plus_b)

        return outputs


x = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x.shape)
y = np.square(x) + 0.5 + noise

#input
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name="x_in")
    ys = tf.placeholder(tf.float32, [None, 1], name="y_in")

l1 = add_layer(xs, 1, 10, activation_fun=tf.nn.relu)
prediction = add_layer(l1, 10, 1, activation_fun=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction), reduction_indices=[1]))

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
writer = tf.summary.FileWriter("d:\logs", sess.graph)
sess.run(init)
