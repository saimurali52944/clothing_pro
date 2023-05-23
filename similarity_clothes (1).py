# -*- coding: utf-8 -*-
"""similarity clothes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1clOWySB9UVII6EfPg86qHd_sb9M1n66W
"""

!pip install sentence-transformers

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
sklearn.metrics.pairwise.cosine_similarity

df = pd.read_csv('data.csv')

model = SentenceTransformer('bert-base-nli-mean-tokens')

df['embeddings'] = df['Tags'].apply(lambda x: model.encode(x))

for i in range(0,int(df.shape[0])):
  df['embeddings'][i] = np.array(df['embeddings'][i]).reshape(1,-1)

def recommend(inp):
  inp = [inp]
  inp = model.encode(inp)
  inp = inp.reshape(1, -1)
  x = df.shape[0]
  sim = []
  for i in range(0, x):
    n = df['embeddings'][i]
    sim.append(cosine_similarity(n, inp))
  scores = list(enumerate(sim))
  scores = sorted(scores, key=lambda n: n[1], reverse=True)
  scores = scores[1:6]
  recommendations = []
  for score in scores:
    prod_index = score[0]
    name = df['Product Name'].iloc[prod_index]
    link = df['Product URL'].iloc[prod_index]
    similarity_score = score[1].item()
    recommendation = {
      "Product Name": name,
      "Link": link,
      "Scores": similarity_score
    }
    recommendations.append(recommendation)
  return recommendations
recommend(input("Search for clothes : "))

