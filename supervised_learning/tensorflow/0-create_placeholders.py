#!/usr/bin/env python3
import tensorflow.compat.v1 as tf

def create_placeholders():
    /// simple example for supervised learning
    x = tf.placeholder(tf.float32, shape=(None, 784), name='x')
    y = tf.placeholder(tf.float32, shape=(None, 10), name='y')
    return x, y