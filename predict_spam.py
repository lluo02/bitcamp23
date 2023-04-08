import os

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.utils import to_categorical

tok = Tokenizer(num_words=10000)


def RNN():
    inputs = Input(name='inputs',shape=[150])
    layer = Embedding(10000,50,input_length=150)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256,name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.5)(layer)
    layer = Dense(1,name='out_layer')(layer)
    layer = Activation('sigmoid')(layer)
    model = Model(inputs=inputs,outputs=layer)
    return model
#model = RNN()

def tokenize(input):
    
    tok.fit_on_texts(input)
    sequences = tok.texts_to_sequences(input)
    sequences_matrix = sequence.pad_sequences(sequences,maxlen=150)
    return sequences_matrix

def predict_spam(input):
    model = keras.models.load_model("spam_model")
    txts = tok.texts_to_sequences(input)
    txts = sequence.pad_sequences(txts, maxlen=150)
    preds = model.predict(txts)
    return preds