#!/usr/bin/env python
# -*- coding: utf-8 -*-

import DBUtil
from jieba import analyse
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags
# 使用自定义停用词集合
stopwords = {}.fromkeys([ line.rstrip() for line in open('C:\Workspace\stopwords.txt') ])
# 原始文本
text = ""

# 基于TF-IDF算法进行关键词抽取
keywords = tfidf(text)
print "keywords by tfidf:"
# 输出抽取出的关键词
final = ''
for keyword in keywords:
	keyword = keyword.encode('gbk')
	if keyword not in stopwords:
		final += keyword +'/'
print final
