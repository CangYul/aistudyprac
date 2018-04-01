# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.lda import LDA
mnist = input_data.read_data_sets("Mnist_data/",one_hot=False)
data_train = mnist.train.images
label_train = mnist.train.labels
data_test = mnist.test.images
label_test = mnist.test.labels

data_train[data_train > 0] = 1
data_test[data_test > 0] = 1
print(data_train.shape)
