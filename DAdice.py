import random
import nltk
from nltk.tokenize import sent_tokenize
from nltk.cluster.util import cosine_distance
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize, ne_chunk, pos_tag
from nltk.tree import Tree
import difflib
from flask import Flask, request, render_template
import re

whole_dictionary = open("english.txt","r")
dictionary = whole_dictionary.readlines()
dictionary = [x.strip() for x in dictionary]
dictionary = [x for x in dictionary if x.isalpha()]

a_words = [t for t in dictionary if t.startswith('a')]
b_words = [t for t in dictionary if t.startswith('b')]
c_words = [t for t in dictionary if t.startswith('c')]
d_words = [t for t in dictionary if t.startswith('d')]
e_words = [t for t in dictionary if t.startswith('e')]
f_words = [t for t in dictionary if t.startswith('f')]
g_words = [t for t in dictionary if t.startswith('g')]

a_pos = nltk.pos_tag(a_words)
b_pos = nltk.pos_tag(b_words)
c_pos = nltk.pos_tag(c_words)
d_pos = nltk.pos_tag(d_words)
e_pos = nltk.pos_tag(e_words)
f_pos = nltk.pos_tag(f_words)
g_pos = nltk.pos_tag(g_words)

a = list()
for item in a_pos:
    if item[1] == 'VBG':
        a.append(item[0])
a = set(a)

b = list()
for item in b_pos:
    if item[1] == 'VBG':
        b.append(item[0])
b = set(b)

c = list()
for item in c_pos:
    if item[1] == 'VBG':
        c.append(item[0])
c = set(c)

d = list()
for item in d_pos:
    if item[1] == 'VBD':
        d.append(item[0])
d = set(d)

e = list()
for item in e_pos:
    if item[1] == 'RB':
        e.append(item[0])
e = set(e)

f = list()
for item in f_pos:
    if item[1] == 'JJ':
        f.append(item[0])
f = set(f)

g = list()
for item in g_pos:
    if item[1] == 'NN':
        g.append(item[0])
g = set(g)