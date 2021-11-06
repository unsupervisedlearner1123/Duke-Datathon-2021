#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans

#%%
df = pd.read_parquet("../20_intermediate_files/mergeddata.parquet")

#%%
q_cols = [col for col in df.columns if col.startswith("q")]

#%%
subset = df[q_cols]

#%%
ohe_subset = pd.get_dummies(subset)

#%%

hc = AgglomerativeClustering(n_clusters=3)
preds = hc.fit_predict(ohe_subset)

#%%
ohe_subset.groupby(preds).mean().T.style.background_gradient(cmap='summer_r')

#%%
km = KMeans(n_clusters=3)
preds_km = km.fit_predict(ohe_subset)

#%%
ohe_subset.groupby(preds_km).mean().T.style.background_gradient(cmap='summer_r')
