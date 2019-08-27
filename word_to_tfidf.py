# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:01:19 2019

@author: humingzhe
"""
import pandas as pd
import jieba
from gensim import corpora, models, similarities
from gensim.matutils import corpus2dense   
import numpy as np

def concat_frame(*args):
    return pd.concat([*args])

'''
def cutwords_frame(frame):
    for i in frame['content']:
        frame.iloc[i,1] = jieba.cut(i)
    return frame

ct = cutwords_frame(a)
'''
#切词 传入
def splitword(comment):
    f = open(r'.\stopwords.txt', 'r+', encoding='utf-8')
    sw = f.read()
    stop_word = sw.splitlines()
    texts = []
    for i in range(len(comment)):
        seg_select =[]
        segs = jieba.cut(comment[i])
        for seg in segs:
            if seg not in stop_word:
                seg_select.append(seg)
        texts.append(seg_select)
    return texts

#t = splitword(a['content'])
'''
def mergect(content):
    ct = []
    for i in content:
        for j in i:
            ct.append(j)
    return ct

k = mergect(t)
'''
def tfidfmodel(texts):
    #生成字典
    dictionary = corpora.Dictionary(texts)
    #词袋模型 对应的稀疏向量的表达
    corpus = [dictionary.doc2bow(text) for text in texts]
    #TFIDF
    tfidf_model = models.TfidfModel(corpus)
    #将文档转化成tf-idf模式表示的向量
    corpus_tfidf = tfidf_model[corpus]
    tf_matrix = corpus2dense(corpus_tfidf, len(dictionary))
    #tf_matrix.shape
    #tfidf = pd.DataFrame(tf_matrix.T)    
    return tf_matrix

#h = tfidfmodel(t)

def frame_add_word(frame,word):
    content_list = list(frame['content'])
    content_list.append(word)
    return content_list
    
def calculate_cor(frame,content_tfidf):
    import numpy as np
    cor = np.corrcoef(content_tfidf.T)[-1][:-1]
    frame['cor'] = cor
    sort_by_cor = frame.sort_values('cor',ascending=False)
    ti_cor_ad = sort_by_cor.loc[:,['title','cor','address']]
    return ti_cor_ad

