# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 22:48:12 2022

@author: debor
"""


import pandas as pd
import gensim
from gensim.models import Word2Vec


df = pd.read_json('final_data.json')

sentences = df.text
clean_data = sentences.dropna()

reviewText = clean_data.apply(gensim.utils.simple_preprocess)

model = gensim.models.Word2Vec(sentences=reviewText, window=5, 
        min_count=10,
        workers=4)

model.save("modelNeeew.kv")

