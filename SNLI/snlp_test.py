# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:22:10 2021

@author: meika
"""

from stanfordcorenlp import StanfordCoreNLP
import re
nlp = StanfordCoreNLP('F:\\Code\\nlp\\stanford-corenlp-latest\\stanford-corenlp-4.3.1')
string = 'This is an example of tokenziation.'
nlp.word_tokenize('This is an example of tokenziation.')
print(nlp.word_tokenize('This is an example of tokenziation.'))

nlp.pos_tag('This is an example of tokenziation.')
print('词性标注：',nlp.pos_tag('This is an example of tokenziation.'))

#print ('句法成分分析:',nlp.parse('This is an example of tokenziation.'))
string = nlp.parse('This is an example of tokenziation.')
result = string
#print(string)
result = result.replace('\n', '')
result = re.sub(' +',' ', result)
print(result)

def parse_sentence(sentence):
    sentence = regex.sub('', sentence)

    result = nlp.parse(sentence)
    result = result.replace('\n', '')
    result = result.replace('\r', '')
    result = re.sub(' +',' ', result)

    #nlp.close() # Do not forget to close! The backend server will consume a lot memery.
    return result.encode("utf-8")

print(parse_sentence('This is an example of tokenziation.'))
#print(string)

#print('dependency_parse:',nlp.dependency_parse(string))

#print('ner:',nlp.ner(string))

#print('word_tokenize:',nlp.word_tokenize(string))
nlp.close()