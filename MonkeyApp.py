# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:22:07 2022

@author: monish
"""
from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# All class labels
class_list = ['Bald Uakari',
 'Emperor Tamarin',
 'Golden Monkey',
 'Gray Langur',
 'Hamadryas Baboon',
 'Mandril',
 'Proboscis Monkey',
 'Red Howler',
 'Vervet Monkey',
 'White Faced Saki']

# Loading trained model file
model = tf.keras.models.load_model('MonkeyClassification.h5',
       custom_objects={'KerasLayer':hub.KerasLayer}
)

def predict(image_path, model):
    img = image.load_img(image_path, target_size = (256,256))
    x=image.img_to_array(img)
    x=x/255
    x=tf.expand_dims(x,axis=0)
    a=np.argmax(model.predict(x))
    return class_list[a]

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'Uploads', secure_filename(f.filename))
        
        f.save(file_path)

        # Make prediction
        preds = predict(file_path, model)

    return preds

if __name__ == '__main__':
    app.run(debug=True)
