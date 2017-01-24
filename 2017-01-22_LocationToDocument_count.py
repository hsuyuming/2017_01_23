# -*- coding: utf-8 -*-
import sys
import pymongo
import codecs
from pymongo import MongoClient
from collections import OrderedDict
from datetime import datetime

# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # 想法：先從project_location_name.txt將地名讀取出來，然後進入MongoDB中查看每篇地名有多少篇文章
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#
#
#
# client=MongoClient('mongodb://10.120.37.128:27017/')
# db = client['family']
# # print db.collection_names()
# travel = db["travel"]
# s1 = datetime.now()
# test_list=[]
# def find_document_count(name):
#     test_dist={}
#     find_contain_keyword_list=list(db.travel.find({'content':{'$regex':name}}))
#     test_dist[name]=len(find_contain_keyword_list)
#     test_list.append(test_dist)
#
#
# myfile=codecs.open('project_location_name.txt','rb','utf-8')
# readfiles=myfile.readlines()
# for x in readfiles:
#     name=x.strip()
#     find_document_count(name)
# for z in test_list:
#     print (z.items()[0][0]+' '+str(z.items()[0][1]))
# s2 = datetime.now()


# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # 目前遇到問題：
# # 1.目前文章有7萬多篇無法對應到我們所找的一千多的景點，該如何把文章和景點對應起來
# # 2.發現7萬多篇的文章有重複性，該如何塞除
# # 解決問題想法：
# # 1.利用tf-idf找出地名 作法：將tfidf_document的字拿去跑程式，先選放進去的字出來有title的
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # 小試結果：
# #蓮荷園休閒農場 蓮荷 4 13
# # 照門休閒農業區 照門 1 29 相關字詞：金谷農場、九芎湖
# # 中央大學 中央大學 10 77
# # 桃園市第一河濱公園 桃園市第一河濱公園 1 1
# # 三民運動公園 三民運動公園 2 15
# # 三民運動公園 三民公園 2 32
# # 小星星義大利麵餐廳 小星星義大利麵 5 5
# # 眷村故事館 眷村故事館 2 13
# # 同安親子公園 1 5
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝


# client=MongoClient('mongodb://10.120.37.128:27017/')
# db = client['family']
# # print db.collection_names()
# travel = db["travel"]
# #
# name=u"小橋"
#
# find_title_list=list(db.travel.find({'title':{'$regex':name}}))
# find_content_list=list(db.travel.find({'content':{'$regex':name}}))
# print len(find_title_list)
# print len(find_content_list)
# for x in find_title_list:
#     print x['title']
#     # print x['content']
# # for x1 in find_content_list:
# #     print x1['title']
# #     print x1['content']

# # ＝＝＝＝＝＝＝
# # 第一步：先將tiidf_document中字部分抓出來（即不要權重），寫成tfidf_only_location.txt的檔案
# # ＝＝＝＝＝＝＝
# myfile_tfidf=codecs.open('tfidf_document.txt','rb','utf-8')
# readfiles=myfile_tfidf.readlines()
# with codecs.open('tfidf_only_location.txt',"w",'utf-8') as location:
#     for location_name in readfiles:
#         location.write(location_name.strip().split(' ')[0]+ '\n')

# # ＝＝＝＝＝＝＝
# # 第二步：將tfidf_only_location.txt做排序，並手動人工刪除數字的部分
# # ＝＝＝＝＝＝＝
# myfile_tfidf2=codecs.open('tfidf_only_location.txt','rb','utf-8')
# readfiles=myfile_tfidf2.readlines()
# readfiles.sort()
# with codecs.open('tfidf_only_location_sorted_nonum.txt',"w",'utf-8') as location:
#     for item in readfiles:
#         location.write(item)

# # ＝＝＝＝＝＝＝
# # 第三步：將tfidf_only_location_sorted_nonum.txt，清除重複過的字，以及在做一次排序
# # ＝＝＝＝＝＝＝
#
# myfile_tfidf3=codecs.open('tfidf_only_location_sorted_nonum.txt',"rb",'utf-8')
# readfiles3=myfile_tfidf3.readlines()
# readfiles3_after=set(readfiles3)
# with codecs.open('tfidf_only_location_clean.txt',"w",'utf-8') as location:
#     for dicts in readfiles3_after :
#         location.write(dicts)
#
# myfile_tfidf4=codecs.open('tfidf_only_location_clean.txt','rb','utf-8')
# readfiles4=myfile_tfidf4.readlines()
# readfiles4.sort()
# with codecs.open('tfidf_only_location_clean.txt',"w",'utf-8') as location:
#     for item in readfiles4:
#         location.write(item)


# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 作法：將tfidf_only_location_clean.txt的字，放入function中，找出在資料中title數量大於1的量有多少
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# # # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
s1 = datetime.now()
client=MongoClient('mongodb://10.120.37.128:27017/')
db = client['family']
travel = db["travel"]


location_list=[]
def infer_name(name):
    location_dist={}
    find_title_list=list(db.travel.find({'title':{'$regex':name}}))
    if len(find_title_list) > 0 :
        location_dist[name]=len(find_title_list)
        location_list.append(location_dist)


myfile_tfidf5=codecs.open('tfidf_only_location_clean.txt','rb','utf-8')
readfiles5=myfile_tfidf5.readlines()
for name in readfiles5:
    name=name.strip()
    infer_name(name)

with codecs.open('test.txt',"w",'utf-8') as location:
    for iii in location_list:
        for i in iii.items():
            location.write(i[0] + ' ' + str(i[1])+'\n')

s2 = datetime.now()

print s2-s1
