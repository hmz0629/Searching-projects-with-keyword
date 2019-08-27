# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:37:07 2019

@author: humingzhe
"""

from urllib import request  
from bs4 import BeautifulSoup            #Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库  
import urllib
import urllib.request as urllib2
import pandas as pd
import re 

class crawling(object):
    def __init__(self,page,word,agent):
        self.page = page
        self.word = word
        self.agent = agent
    
    def analy_web(self,url,headers):
        _page = request.Request(url,headers=headers)  
        page_info = request.urlopen(_page).read().decode('utf-8')#打开Url,获取HttpResponse返回对象并读取其ResposneBody      
        # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器  
        soup = BeautifulSoup(page_info, 'html.parser') 
        return soup        
    
    def gitee_search(self):
        baseUrl = 'https://gitee.com/search'
        data = {'q':self.word,'page':str(self.page-1),'utf8':'✓'}
        data = urllib.parse.urlencode(data)
        url = baseUrl+'?'+data
        #构造头文件，模拟浏览器访问  
        headers = {'User-Agent':self.agent}  
        soup = self.analy_web(url,headers)
        # 以格式化的形式打印html  
        #print(soup.prettify())      
        items = soup.find_all('a',attrs={'class':'ellipsis'})
        cc = soup.find_all('div','description') #describe
        ct,bt,ad = [],[],[]
        for i in cc:
            ct.append(re.sub('<.*?>|\\n','',str(i)))
        for i in items:
            ad.append('https://gitee.com'+i.get('href'))
            bt.append(i.get('title'))
        result = pd.DataFrame({'title':bt,'content':ct,'address':ad})
        return result     
    
    def oschina_search(self):
        baseUrl = 'https://www.oschina.net/search'
        data = {'q':self.word,'p':str(self.page-1)}
        data = urllib.parse.urlencode(data)
        url = baseUrl+'?'+data
        headers = {'User-Agent':self.agent}  
        soup = self.analy_web(url,headers)
        # 以格式化的形式打印html  
        items = soup.find_all('div',attrs={'class':'ui relaxed items list-container search-list-container'})
        content = soup.find_all('div','content')
        bt,ct,ad = [],[],[]
        pattern = '<.*?>|\[|\]'
        for i in content:
            ad.append(re.sub(pattern,'',str(i.find_all('div',attrs={'class':'meta'})))) #address
            ct.append(re.sub(pattern,'',str(i.find_all('p',attrs={'class':'line-clamp'})))) #describe
            bt.append(re.sub(pattern,'',str(i.find_all('span',attrs={'class':'project-title'})))) #title
        result = pd.DataFrame({'title':bt,'content':ct,'address':ad})
        return result                   

if '__name__' == '__main__':
    page = 2
    word = '机器学习 深度学习'
    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    frame = crawling(page,word,agent)
    a = frame.oschina_search()
    b = frame.gitee_search()
