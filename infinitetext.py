mport random
import nltk
from nltk.tokenize import sent_tokenize
from nltk.cluster.util import cosine_distance
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize, ne_chunk, pos_tag
from nltk.tree import Tree
import difflib
from flask import Flask, request, render_template
import re
from nltk.util import ngrams

text1 = "3 start I want to start here but it wouldn't let me do what I want with my sentence. The exact neural mechanism underlying such long-term cognitive hindsight bias would be different from that which underlies perceptual backward phenomena on the microscopic time scale."
text = "3 night Last night I dreamt I went to Manderley again. It seemed to me I stood by the iron gate leading to the drive, and for a while I could not enter, for the way was barred to me. There was a padlock and chain upon the gate. I called in my dream to the lodge-keeper, and had no answer, and peering closer through the rusted spokes of the gate I saw that the lodge was uninhabited."
words = text.split()
character_history_size = int(words[0])
start_seed = words[1]
del words[0]
del words[0]
words = ' '.join(words)


def MarkovText():
chars = list(words)
output = start_seed

combos = list(ngrams(chars, character_history_size))
seed = start_seed[-(character_history_size - 1):]
sentences = []

sentence_counter = 0
while sentence_counter < 3:
    lst = combos
    for i in range(len(seed)):
        lst = [item for item in lst if item[i]==seed[i]]
    next_state = random.sample(lst, 1)[0][-1]
    output += next_state
    seed = output[-(character_history_size - 1):]
    if next_state == '.':
        sentence_counter += 1
        sentences.append(output)
        word_bank = [word for word in output.split() if len(word) > character_history_size]
        output = random.sample(word_bank, 1)[0]
        seed = output[-(character_history_size - 1):]
print sentences