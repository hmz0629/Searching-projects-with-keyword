# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:35:05 2019

@author: humingzhe
"""
import numpy as np
from search_web import *
from word_to_tfidf import *

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
'''
def frame_add_word(frame,word):
    content_list = list(frame['content'])
    content_list.append(word)
    return content_list
    
def calculate_cor(frame,content_tfidf):
    cor = np.corrcoef(content_tfidf.T)[-1][:-1]
    concat['cor'] = cor
    sort_by_cor = concat.sort_values('cor',ascending=False)
    ti_cor_ad = sort_by_cor.loc[:,['title','cor','address']]
    return ti_cor_ad
'''

def run(page,word,agent):
    frame = crawling(page,word,agent)
    a = frame.oschina_search()
    b = frame.gitee_search()
    concat = concat_frame(a,b)
    l_cont = frame_add_word(concat,word)
    cut_content = splitword(l_cont)
    content_tfidf = tfidfmodel(cut_content)
    return calculate_cor(concat,content_tfidf)

if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    page = 1
    print("Enter Your keywords：")
    word = input()
    print(run(page,word,agent))
