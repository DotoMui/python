# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:24:26 2021

@author: meika
"""

from nltk import Tree
from functools import reduce

def binarize(tree):
    """
    Recursively turn a tree into a binary tree.
    """
    if isinstance(tree, str):
        return tree
    elif len(tree) == 1:
        return binarize(tree[0])
    else:
        label = tree.label()
        return reduce(lambda x, y: Tree(label, (binarize(x), binarize(y))), tree)
        #return reduce(lambda x, y: (binarize(x), binarize(y)), tree)

t = Tree.fromstring('(ROOT (S (NP (DT This)) (VP (VBZ is) (NP (NP (DT an) (NN example)) (PP (IN of) (NP (NN tokenziation)))))))')
bt = binarize(t)


import re
import string
from stanfordcorenlp import StanfordCoreNLP
from nltk import Tree
from functools import reduce
'''
regex = re.compile('[%s]' % re.escape(string.punctuation))

def parse_sentence(sentence):
    nlp = StanfordCoreNLP(r'./stanford-corenlp-full-2018-02-27')
    sentence = regex.sub('', sentence)

    result = nlp.parse(sentence)
    result = result.replace('\n', '')
    result = re.sub(' +',' ', result)

    nlp.close() # Do not forget to close! The backend server will consume a lot memery.
    return result.encode("utf-8")
'''
def binarize2(sentence):
    sentence = sentence.replace("\n", "")

    for pattern in ["ROOT", "SINV", "NP", "S", "PP", "ADJP", "SBAR", 
                    "DT", "JJ", "NNS", "VP", "VBP", "RB","CD","BAR","IN","VBG"]:
        sentence = sentence.replace("({}".format(pattern), "(")

    sentence = re.sub(' +',' ', sentence)
    return sentence
bp = binarize2(str(bt))
'''
( ( Two woman ) ( ( are ( holding packages ) ) . ) )
( ( ( Two woman) ( are ( holding packages))) .)
'''
