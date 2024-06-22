import random
import string
import dill as pickle
import tensorflow as tf
import tensorflow as tf
from keras.layers import deserialize
import tensorflow as tf
import os
import numpy as np
from tensorflow.keras.preprocessing import image

# Prétraitement des images
def preprocess_image(file):
    img = image.load_img(file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Ajouter la dimension de batch
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)  # Prétraiter pour EfficientNet
    return img_array

model = tf.saved_model.load("model_tf")
model = model.signatures['serving_default']

def valid_db(file):
  

    img = preprocess_image(file)
    output = model(tf.constant(img))
    predicted = output['dense_5']  # Assurez-vous que 'dense' correspond à la sortie correcte de votre modèle
    
    if predicted.numpy()[0][0] >= 0.51:
      return "2"
    
    else:
      x = list(string.printable)
      random.shuffle(x)
      buff = []
      for i in range(len(x)):
        buff.append(x[i]if x[i] not in ['\u000b', '\t', '\n'] else '')
      return ''.join(buff), 400
