import random
import nltk
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize, ne_chunk, pos_tag
from textblob import TextBlob
import csv

file = open('PUPPETLines.txt', 'r')
results = file.readlines()
results = [x.decode('utf-8') for x in results]
results = [TextBlob(x) for x in results]

scores = [x.sentiment.polarity for x in results]
mylist = zip(results, scores)
sorted_list = sorted(mylist, key=lambda couplet: couplet[1])

negative_5 = [str(x[0]) for x in sorted_list[0:40]]
negative_4 = [str(x[0]) for x in sorted_list[40:80]]
negative_3 = [str(x[0]) for x in sorted_list[80:120]]
negative_2 = [str(x[0]) for x in sorted_list[120:160]]
negative_1 = [str(x[0]) for x in sorted_list[160:200]]
zero = [str(x[0]) for x in sorted_list[200:240]]
positive_1 = [str(x[0]) for x in sorted_list[240:280]]
positive_2 = [str(x[0]) for x in sorted_list[280:320]]
positive_3 = [str(x[0]) for x in sorted_list[320:360]]
positive_4 = [str(x[0]) for x in sorted_list[360:400]]
positive_5 = [str(x[0]) for x in sorted_list[400:440]]