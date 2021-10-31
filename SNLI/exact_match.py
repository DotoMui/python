# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 21:17:04 2021

@author: meika
"""
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('F:\\Code\\nlp\\stanford-corenlp-latest\\stanford-corenlp-4.3.1')
sentence1 = 'A younger man dressed in tribal attire.'
sentence2 = 'A young man wheres tribal clothes for a ceremony.'

def exact_match(sentence1,sentence2): #sentence2变成字典 sentence1=sentence2=[word1,word2]
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()
    sentence1 = nlp.word_tokenize(sentence1)
    sentence2 = nlp.word_tokenize(sentence2)
    
    q_words_cased = {w for w in sentence2}
    ls = []
    for i in range(len(sentence1)):
        if sentence1[i] in q_words_cased:
            ls.append(i)
    return ls

ls1 = exact_match(sentence1,sentence2)
ls2 = exact_match(sentence2,sentence1)

example = {'sentence1_token_exact_match_with_s2':ls1,\
           'sentence2_token_exact_match_with_s1':ls2}

nlp.close()