#!/usr/bin/python
# Copyright (C) 2017  Shannon Wang and Emily Wang
#
###############################################################################
#
# IMPORT MODULES
#
###############################################################################

import random
import nltk
import string
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

###############################################################################
#
# BEGIN CODE
#
###############################################################################

options = [1, 2, 3, 4]

def synonym(word):
    myword = wn.synsets(word)
    if len(myword) > 0:
        myword = myword[0]
        return [(s.name()).partition('.')[0] for s in myword.lemmas()]
    else:
        return myword

def antonym(word):
    myword = wn.synsets(word)
    if len(myword) > 0:
        myword = myword[0]
        return [(s.name()).partition('.')[0] for s in (myword.lemmas()[0]).antonyms()]
    else:
        return myword

def hyponym(word):
    myword = wn.synsets(word)
    if len(myword) > 0:
        myword = myword[0]
        return [(s.name()).partition('.')[0] for s in myword.hyponyms()]
    else:
        return myword
    
def hypernym(word):
    myword = wn.synsets(word)
    if len(myword) > 0:
        myword = myword[0]
        return [(s.name()).partition('.')[0] for s in myword.hypernyms()]
    else:
        return myword    

def operation(option, word):
    if option == 1:
        return synonym(word)
    elif option == 2:
        return antonym(word)
    elif option == 3:
        return hyponym(word)
    else:
        return hypernym(word)

def positive_replacement(word, replacements):
    positive_score = swn.senti_synsets(word)[0].pos_score()
    negative_score = swn.senti_synsets(word)[0].neg_score()
    suitable_replacements = []
    for replacement in replacements:
        replacement_pos_score = swn.senti_synsets(replacement)[0].pos_score()
        replacement_neg_score = swn.senti_synsets(replacement)[0].neg_score()
        if replacement_pos_score > positive_score or replacement_neg_score < negative_score:
            suitable_replacements.append(replacement)
    return suitable_replacements

def negative_replacement(word, replacements):
    positive_score = swn.senti_synsets(word)[0].pos_score()
    negative_score = swn.senti_synsets(word)[0].neg_score()
    suitable_replacements = []
    for replacement in replacements:
        replacement_pos_score = swn.senti_synsets(replacement)[0].pos_score()
        replacement_neg_score = swn.senti_synsets(replacement)[0].neg_score()
        if replacement_pos_score < positive_score or replacement_neg_score > negative_score:
            suitable_replacements.append(replacement)
    return suitable_replacements

text = "Hard by a great forest dwelt a wood-cutter with his wife, who had an only child, a little girl three years old.  They were so poor, however, that they no longer had daily bread, and did not know how to get food for her.  One morning the wood-cutter went out sorrowfully to his work in the forest, and while he was cutting wood, suddenly there stood before him a tall and beautiful woman with a crown of shining stars on her head, who said to him 'I am the virgin mary, mother of the child jesus. You are poor and needy, bring your child to me, I will take her with me and be her mother, and care for her.' The wood-cutter obeyed, brought his child, and gave her to the virgin mary, who took her up to heaven with her.  There the child fared well, ate sugar-cakes, and drank sweet milk, and her clothes were of gold, and the little angels played with her."
disjointed_words = word_tokenize(text)
pos_output = word_tokenize(text)
neg_output = word_tokenize(text)
tagged_words = pos_tag(disjointed_words)
nouns = []
adjectives = []
for i in range(len(tagged_words)):
    if tagged_words[i][1] == 'NN' or tagged_words[i][1] == 'NNS':
        nouns.append((i, tagged_words[i][0]))
    elif tagged_words[i][1][:2] == 'JJ':
        adjectives.append((i, tagged_words[i][0]))
words_to_be_replaced = nouns + adjectives
if len(words_to_be_replaced) == 0:
    print "Try again with nouns and adjectives in your text."
else:
    for (index, word) in words_to_be_replaced:
       order = random.sample(options, 4)
       replacements = operation(order[0], word)
       if len(replacements) > 0:
           pos_replacements = positive_replacement(word, replacements)
           neg_replacements = negative_replacement(word, replacements)
           if len(pos_replacements) > 0 and len(neg_replacements) > 0:
               continue
           elif len(pos_replacements) == 0 and len(neg_replacements) > 0:     
                replacements = operation(order[1], word)
		pos_replacements = positive_replacement(word, replacements)
		if len(pos_replacements) == 0:
                    replacements = operation(order[2], word)
                    pos_replacements = positive_replacement(word, replacements)
                if len(pos_replacements) == 0:
                    replacements = operation(order[3], word)
                    pos_replacements = positive_replacement(word, replacements)
           elif len(pos_replacements) > 0 and len(neg_replacements) == 0:
                replacements = operation(order[1], word)
		neg_replacements = negative_replacement(word, replacements)
		if len(neg_replacements) == 0:
                    replacements = operation(order[2], word)
                    neg_replacements = negative_replacement(word, replacements)
                if len(neg_replacements) == 0:
                    replacements = operation(order[3], word)
                    neg_replacements = negative_replacement(word, replacements)
           else:
                replacements = operation(order[1], word)
		pos_replacements = positive_replacement(word, replacements)
		if len(pos_replacements) == 0:
                    replacements = operation(order[2], word)
                    pos_replacements = positive_replacement(word, replacements)
                if len(pos_replacements) == 0:
                    replacements = operation(order[3], word)
                    pos_replacements = positive_replacement(word, replacements)
		neg_replacements = negative_replacement(word, replacements)
		if len(neg_replacements) == 0:
                    replacements = operation(order[2], word)
                    neg_replacements = negative_replacement(word, replacements)
                if len(neg_replacements) == 0:
                    replacements = operation(order[3], word)
                    neg_replacements = negative_replacement(word, replacements)
           #print index, word, pos_replacements
           #print index, word, neg_replacements
           if len(pos_replacements) > 0:
               pos_word = pos_replacements[0]
               #print pos_word
               pos_output[index] = pos_word
               #print pos_output[index]
               #print pos_output
           if len(neg_replacements) > 0:
               neg_word = neg_replacements[0]
               #print neg_word
               neg_output[index] = neg_word
               #print neg_output[index]
       else:
           continue
    pos_output = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in pos_output]).strip()
    neg_output = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in neg_output]).strip()
    print pos_output
    print neg_output
