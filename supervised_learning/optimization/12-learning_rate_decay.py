#!/usr/bin/env python3
"""
Defines function that creates a learning rate decay op
for a neural network in TensorFlow using inverse time decay
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


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    Creates a learning rate decay op for a neural network in TensorFlow
        using inverse time decay

    parameters:
        alpha [float]: original learning rate
        decay_rate: wight used to determine the rate at which alpha will decay
        global_step [int]:
            number of passes of gradient descent that have elapsed
        decay_step [int]:
            number of passes of gradient descent that should occur before
                alpha is decayed furtherXS

    the learning rate decay should occur in a stepwise fashion

    returns:
        the learning rate decay operation
    """
    op = tf.train.inverse_time_decay(
        alpha, global_step, decay_step, decay_rate, staircase=True)
<<<<<<< HEAD
<<<<<<< HEAD
    return op
=======
    return op
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
=======
    return op
>>>>>>> 8df1b1cde11557e77d0ddcb331fc2f85786c7886
