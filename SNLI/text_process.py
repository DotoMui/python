# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:18:04 2021

@author: meika
"""

import pandas as pd
import re
import string
from stanfordcorenlp import StanfordCoreNLP
from nltk import Tree
from functools import reduce
import ast
import jsonlines


'''
return (ROOT (S (NP (DT This)) (VP (VBZ is) (NP (NP (DT an) (NN example)) (PP (IN of) (NP (NN tokenziation)))))))
'''
def parse(result):
    #result = nlp.parse(result)
    result = result.replace('\n', '')
    result = result.replace('\r', '')
    result = re.sub(' +',' ', result)
    return result


'''
binarize
'''
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


'''
return ( This ( is ( ( an example) ( of tokenziation))))
'''    
def binary_parse(sentence):
    #sentence = nlp.parse(sentence)
    t = Tree.fromstring(sentence)
    sentence = str(binarize(t))
    sentence = sentence.replace("\n", "")
    
    #for pattern in ["ROOT", "SINV", "NP", "S", "PP", "ADJP", "SBAR", 
    #               "DT", "JJ", "NNS", "VP", "VBP", "RB","CD","BAR","IN","VBG","FRAG","Q"]:
    for pattern in Pos_dict:
        sentence = sentence.replace("({}".format(pattern), "(")

    sentence = re.sub(' +',' ', sentence)
    return sentence

'''
return [0,2,5,7]
'''
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

nlp = StanfordCoreNLP('F:\\Code\\nlp\\stanford-corenlp-latest\\stanford-corenlp-4.3.1')
'''
举例测试

#regex = re.compile('[%s]' % re.escape(string.punctuation))
sentence1 = 'A younger man dressed in tribal attire.'
sentence2 = 'A young man wheres tribal clothes for a ceremony.'
#sentence1 = regex.sub('', sentence1) 

sentence1_parse = parse(sentence1)  #去掉回车和换行符
sentence1_binary_parse = binary_parse(sentence1)

sentence1_token_exact_match_with_s2 = exact_match(sentence1,sentence2)
sentence2_token_exact_match_with_s1 = exact_match(sentence2,sentence1)
'''

#词性字典
Pos_dict = []
with open("./Pos.txt", errors='ignore',encoding="utf-8") as f:
    for line in f.readlines():
        Pos_dict.append(line.strip())
        
file_name = 'COVID-19'
df = pd.read_excel("./data/xls/"+file_name+".xls")
'''
#1.数据清洗
'''
#ls = ["BBC What's New", 'whats new bbc', "what's new bbc", "bbc africa what's new", 'BBC Africa', 'BBC News', 'BBC kids', "bbc children's", 'Africa', 'african', 'good news', 'african news', 'arab spring', 'tunisia arab spring', 'tunisia protests', 'middle east']
#str_ls = ",".join(ls)
# ast.literal_eval(df['tags'][0]) 字符串读取识别为list
url_pattern = re.compile(r'(?:\@|http?\://|https?\://|www)\S+')
word_pattern = re.compile(r'[^a-zA-Z|\s|\,]') #保留英文，和list需要的格式字符
wrong_pattern = re.compile(r'[%]')
df = df.dropna(axis=0,subset = ["title", "tags"])   # 丢弃"title", "sentence2"这两列中有缺失值的行
df['sentence2'] = df['tags'].apply(ast.literal_eval).apply(lambda x:",".join(x[:3])).apply(lambda x: re.sub(wrong_pattern, '',x) if pd.isna(x) != True else x) #ast.literal_eval:转list list取前3个 组成字符串
#df['tags'] = df['tags'].apply(lambda x: re.sub(url_pattern, '', x) if pd.isna(x) != True else x)    #去掉网页
#df['tags'] = df['tags'].apply(lambda x: re.sub(word_pattern, '', x) if pd.isna(x) != True else x)   #保留英文，和list需要的格式字符
#df['sentence2'] = df['tags'].apply(ast.literal_eval).apply(lambda x:",".join(x)) #1.先识别为列表 2.list拼接成字符串
df = df.dropna(axis=0,subset = ["title", "sentence2","tags"])   # 丢弃"title", "sentence2"这两列中有缺失值的行
df=df[~df['sentence2'].isin([''])]  #通过~取反，选取不包含数字1的行
df['sentence1'] = df['title'].apply(lambda x: re.sub(wrong_pattern, '',x) if pd.isna(x) != True else x) #出错，要过滤字符
df['tree2'] = 0
df = df.reset_index(drop=True)

'''
2.获得 parse、binary_parse、exact_match
'''
df['tree1'] = df['sentence1'].apply(nlp.parse)
df['tree2'] = df['sentence2'].apply(nlp.parse)

df['sentence1_parse'] = df['tree1'].apply(parse)
df['sentence1_binary_parse'] = df['tree1'].apply(binary_parse)
df['sentence2_parse'] = df['tree2'].apply(parse)
df['sentence2_binary_parse'] = df['tree2'].apply(binary_parse)


'''
# 测试错误

for index,i in enumerate(df['sentence2']):
    if(index>=0):
        print(str(index)+'  '+df['id'][index]+'\n',i)
        nlp.parse(i)
'''
#df['sentence1_binary_parse'].to_csv('filepath.txt', sep='\n', index=False)


'''
# 3.组成新的df保存
'''
#df.columns 组成新的df
new_df = df[['id','title','tags',\
             'sentence1','sentence1_parse','sentence1_binary_parse',\
             'sentence2','sentence2_parse','sentence2_binary_parse']]

with jsonlines.open('./data/jsonl/'+file_name+'.jsonl', mode='w') as writer:
    for i in range(len(new_df)):
        writer.write({'id' : new_df['id'][i],
                      'labels' : file_name,
                      'sentence1' : new_df['sentence1'][i],
                      'sentence1_parse' : new_df['sentence1_parse'][i],
                      'sentence1_binary_parse' : new_df['sentence1_binary_parse'][i],
                      'sentence2' : new_df['sentence2'][i],
                      'sentence2_parse' : new_df['sentence2_parse'][i],
                      'sentence2_binary_parse' : new_df['sentence2_binary_parse'][i],
                      #exact match
                      'sentence1_token_exact_match_with_s2' : exact_match(new_df['sentence1'][i],new_df['sentence2'][i]),
                      'sentence2_token_exact_match_with_s1' : exact_match(new_df['sentence2'][i],new_df['sentence1'][i])
                      })

nlp.close()
