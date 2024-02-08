import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import pad_sequences
import numpy as np
import pickle

languages = ['Arabic', 'Danish', 'Dutch', 'English', 'French', 'German',
       'Greek', 'Hindi', 'Italian', 'Kannada', 'Malayalam', 'Portugeese',
       'Russian', 'Spanish', 'Sweedish', 'Tamil', 'Turkish']

def get_predictions(sentence):

    if sentence != None:
        tokenizer_path = 'lang_detect_tokenizer.pkl'
        with open(tokenizer_path, 'rb') as tokenizer_file:
            loaded_tokenizer = pickle.load(tokenizer_file)

        model = load_model("language_detection.h5")
        sequences = loaded_tokenizer.texts_to_sequences([sentence])

        padded_seq = pad_sequences(sequences, maxlen = 50)

        predictions = np.argmax(model.predict(padded_seq))
        language_name = languages[predictions]

        print("language_name ----- ",language_name)

        return language_name
    else:
        return None