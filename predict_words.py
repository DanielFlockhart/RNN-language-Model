import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import time



def get_sentance(chars,seed,model,states,next_char,result):
    for n in range(chars):
      next_char, states = model.generate_one_step(next_char, states=states)
      result.append(next_char)
    return tf.strings.join(result)[0].numpy().decode("utf-8")
    
