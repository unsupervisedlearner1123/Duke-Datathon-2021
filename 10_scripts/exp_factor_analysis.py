#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans

#%%
df = pd.read_parquet("../20_intermediate_files/mergeddata.parquet")

#%%
q_cols = [col for col in df.columns if col.startswith("q")]
kick_out = ["q027", "q028"]

#%%
subset = df[(col for col in q_cols if col not in kick_out)].copy()

#%%
for col in subset.columns:
    subset[col] = subset[col].cat.add_categories(["missing"])
    subset[col] = subset[col].fillna("missing")


#%%

from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder()
subset_encoded = oe.fit_transform(subset)
subset_encoded = pd.DataFrame(subset_encoded, columns=subset.columns)

#%%
from sklearn.decomposition import FactorAnalysis

logliks = []
for ncomp in range(2, 10):
    fa = FactorAnalysis(n_components=ncomp)
    fa.fit(subset_encoded)
    logliks.append(fa.score(subset_encoded))

#%%
import numpy as np
plt.plot(range(2, 10), logliks)


#%%
fa = FactorAnalysis(n_components=3)
preds = fa.fit_transform(subset_encoded)

#%%
sns.heatmap(pd.DataFrame(fa.components_, columns=subset_encoded.columns).T, annot=True)

#%%
