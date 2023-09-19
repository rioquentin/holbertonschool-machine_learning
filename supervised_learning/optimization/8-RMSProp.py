#!/usr/bin/env python3
"""
Defines function that creates the training op
for a neural network in TensorFlow using
the RMSProp optimization algorithm
"""


<<<<<<< HEAD
<<<<<<< HEAD
import tensorflow as tf
=======
import tensorflow.compat.v1 as tf
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
=======
import tensorflow.compat.v1 as tf
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    Creates the training operation for a neural network in TensorFlow
        using the RMSProp optimization algorithm

    parameters:
        loss: the loss of the network
        alpha [float]: learning rate
        beta2 [float]: RMSProp weight
        epsilon [float]: small number to avoid division by zero

    returns:
        the RMSProp optimization operation
    """
    op = tf.train.RMSPropOptimizer(
        alpha, decay=beta2, epsilon=epsilon).minimize(loss)
<<<<<<< HEAD
<<<<<<< HEAD
    return op
=======
    return op
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
=======
    return op
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
