import nltk
import urllib
from urllib import urlopen
from nltk import word_tokenize
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import sys
import math
from textblob import TextBlob as tb
from __future__ import division, unicode_literals

reload(sys)
sys.setdefaultencoding('utf8')

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
          'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
          'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
          'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def stemmer(state):
    text_file = open(state+".txt", "r")
    lines = text_file.readlines()
    lines = word_tokenize(lines[0])

    lancaster_stemmer = LancasterStemmer()
    mywords = []
    for word in lines:
        newword = lancaster_stemmer.stem(word)
        mywords.append(newword)

i = 0
dictionary = ['']*50
for state in states:
    # dictionary[i] = stemmer(state)
    text_file = open(state + ".txt", "r")
    lines = text_file.readlines()
    dictionary[i] = tb(lines[0])
    i += 1

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

# tfidf_mat = ['']*50
# j = 0
# for state in states:
#     for word in dictionary[j].split():
#         tfidf_mat[j] = [tfidf_mat[j], tfidf(word, dictionary[j], dictionary)]
#     j += 1

bloblist = dictionary
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))

dict = {"Alabama":['birmingham', 'mobile', 'huntsville'],
        "Alaska":['cdp','anchorage','fairbanks'],
        "Arizona":['tucson','phoenix','maricopa'],
        "Arkansas":['ozark','ouachita','fayetteville'],
        "California":['san','los','angeles'],
        "Colorado":['denver','marijuana','boulder'],
        "Connecticut":['hartford','bridgeport','fairfield'],
        "Delaware":['wilmington','sussex','dover'],
        "Florida":['miami','tampa','orlando'],
        "Georgia":['atlanta','savannah','macon'],
        "Hawaii":['honolulu','maui','polynesian'],
        "Idaho":['boise','lewiston','pocatello'],
        "Illinois":['chicago','rockford','peoria'],
        "Indiana":['indianapolis','evansville','hoosier'],
        "Iowa":['moines','des','dubuque'],
        "Kansas":['wichita','topeka','brownback'],
        "Kentucky":['louisville','bluegrass','lexington'],
        "Louisiana":['orleans','parish','baton'],
        "Maine":['portland','acadia','brunswick'],
        "Maryland":['baltimore','chesapeake','calvert'],
        "Massachusetts":['boston','springfield','cod'],
        "Michigan":['detroit','lansing','peninsula'],
        "Minnesota":['minneapolis','dfl','duluth'],
        "Mississippi":['levees','tupelo','biloxi'],
        "Missouri":['louis','kansas','ozarks'],
        "Montana":['helena','billings','waterbody'],
        "Nebraska":['omaha','unicameral','platte'],
        "Nevada":['vegas','las','reno'],
        "New Hampshire":['manchester','nh','concord'],
        "New Jersey":['bergen','newark','nj'],
        "New Mexico":['fe','albuquerque','santa'],
        "New York":['manhattan','niagara','hudson'],
        "North Carolina":['charlotte','raleigh','greensboro'],
        "North Dakota":['bismarck','minot','fargo'],
        "Ohio":['cincinnati','columbus','toledo'],
        "Oklahoma":['tulsa','cherokee','lawton'],
        "Oregon":['portland','willamette','beaverton'],
        "Pennsylvania":['pittsburgh','philadelphia','erie'],
        "Rhode Island":['providence','newport','island'],
        "South Carolina":['charleston','greenville','spartanburg'],
        "South Dakota":['sioux','rushmore','lakota'],
        "Tennessee":['nashville','memphis','knoxville'],
        "Texas":['houston','dallas','austin'],
        "Utah":['salt','wasatch','provo'],
        "Vermont":['burlington','press','chronicle'],
        "Virginia":['hampton','commonwealth','richmond'],
        "Washington":['seattle','tacoma','spokane'],
        "West Virginia":['charleston','wheeling','morgantown'],
        "Wisconsin":['milwaukee','eau','badger'],
        "Wyoming":['teton','laramie','yellowstone']}