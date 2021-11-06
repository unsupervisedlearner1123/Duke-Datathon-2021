#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

from data_mapping import w1_column_mapping
from data_mapping import w1_response_mapping

#%%

_, meta1 = pyreadstat.read_sav(
    os.path.join("../00_source_data/W1 Merged Data/Wave.1_Data/Merge/Wave1_20170906.sav")
)

_, meta2 = pyreadstat.read_sav(
    os.path.join("../00_source_data/W2 Merged Data/2w-3rd_release_all/merge/Wave2_20170724.sav")
)

#%%
items1_raw = meta1.column_labels
items2_raw = meta2.column_labels

items1_raw = [x for x in items1_raw if x is not None]
items2_raw = [x for x in items2_raw if x is not None]
#%%
from nltk.corpus import stopwords
eng_stopwords = stopwords.words("english")

# remove stopwords
def remove_stopwords(text):
    return " ".join([word for word in text.split() if word.lower() not in eng_stopwords])

items1 = [remove_stopwords(item) for item in items1_raw]
items2 = [remove_stopwords(item) for item in items2_raw]

#%%
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
cv.fit(items1 + items2)

#%%
items1_counts = cv.transform(items1)
items2_counts = cv.transform(items2)

#%%
from sklearn.metrics.pairwise import cosine_similarity
distmtx = cosine_similarity(items1_counts, items2_counts)

#%%
argmaxes = distmtx.argmax(axis=1)

#%%
for idx, argmax in enumerate(argmaxes):
    print(f"{items1_raw[idx]:<60} <==> {items2_raw[argmax]}")