#!/usr/bin/env python3
"""
Defines function that creates the training op
for a neural network in TensorFlow using
the gradient descent with momentum optimization algorithm
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


def create_momentum_op(loss, alpha, beta1):
    """
    Creates the training operation for a neural network in TensorFlow
        using the gradient descent with momentum optimization algorithm

    parameters:
        loss: the loss of the network
        alpha [float]: learning rate
        beta1 [float]: momentum weight

    returns:
        the momentum optimization operation
    """
    op = tf.train.MomentumOptimizer(alpha, beta1).minimize(loss)
<<<<<<< HEAD
<<<<<<< HEAD
    return op
=======
    return op
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
=======
    return op
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
