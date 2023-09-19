#!/usr/bin/env python3
"""
Defines function that creates the training op
for a neural network in TensorFlow using
the Adam optimization algorithm
"""


<<<<<<< HEAD
import tensorflow as tf
=======
import tensorflow.compat.v1 as tf
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """
    Creates the training operation for a neural network in TensorFlow
        using the Adam optimization algorithm

    parameters:
        loss: the loss of the network
        alpha [float]: learning rate
        beta1 [float]: weight used for first moment
        beta2 [float]: weight used for second moment
        epsilon [float]: small number to avoid division by zero

    returns:
        the Adam optimization operation
    """
    op = tf.train.AdamOptimizer(
        alpha, beta1=beta1, beta2=beta2, epsilon=epsilon).minimize(loss)
<<<<<<< HEAD
    return op
=======
    return op
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
