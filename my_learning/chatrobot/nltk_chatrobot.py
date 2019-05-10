import nltk
import numpy as np
import random
import string  # to process standard python strings

f = open('chatbot.txt', 'r', errors='ignore')
raw = f.read()
raw = raw.lower()  # converts to lowercase
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words
print(sent_tokens)
print(word_tokens)
