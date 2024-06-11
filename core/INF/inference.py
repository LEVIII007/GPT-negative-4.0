import keras
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing.image import load_img, img_to_array
import os
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
vgg_model = VGG16()
vgg_model = keras.models.Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)

with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

from keras.models import load_model
import base64
from PIL import Image
import io


model = load_model('img_caption_model.h5')


from PIL import Image
# import matplotlib.pyplot as plt
# generate caption for an image

def idx_to_word(integer, tokenizer):

    # Iterate through the tokenizer's vocabulary
    for word, index in tokenizer.word_index.items():
        # If the integer ID matches the index of a word, return the word
        if index == integer:
            return word

    # If no matching word is found, return None
    return None

def predict_caption(model, image, tokenizer, max_length):
    # add start tag for generation process
    in_text = 'startseq'
    # iterate over the max length of sequence
    for i in range(max_length):
        
       # Tokenize the current caption into a sequence of integers
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        
        # pad the sequence
        sequence = pad_sequences([sequence], max_length)
       
        # predict next word
        yhat = model.predict([image, sequence], verbose=0)
       
        # Get the index of the word with the highest probability
        yhat = np.argmax(yhat)
        
        # convert index to word
        word = idx_to_word(yhat, tokenizer)
        
        # stop if word not found
        if word is None:
            break
        # append word as input for generating next word
        in_text += " " + word
        # stop if we reach end tag
        if word == 'endseq':
            break
      
    return in_text

def new_caption(image, model, tokenizer, max_length):

    # Load VGG16 model and restructure it to output features from the second-to-last layer

    # Load and preprocess the image
    # image = load_img(image_path, target_size=(224, 224))
    image.reshape(224, 224)
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)

    # Extract features from the image using VGG16
    feature = vgg_model.predict(image, verbose=0)

    # Generate caption using the trained model
    caption = predict_caption(model, feature, tokenizer, max_length)

    return caption

import cv2
def process_image(image_data):
    nparr = np.frombuffer(image_data, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(type(img_np))
    print(img_np.shape())
    print(type(img_np))


