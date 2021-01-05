#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: swp
@file: word2vec.py
@time:   2021/1/5
@version:  
"""
from gensim.models import Word2Vec
import gensim,logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
sentences = [['first', 'sentence'], ['second', 'sentence']]
model=Word2Vec(sentences, min_count=1)