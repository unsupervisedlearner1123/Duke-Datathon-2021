#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans

#%%
df = pd.read_parquet("../20_intermediate_files/W1mergeddata.parquet")

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
from sklearn.cluster import KMeans

inertias = []
for n_clus in range(2, 10):
    km = KMeans(n_clusters=n_clus, random_state=42)
    km.fit(subset_encoded)
    inertias.append(km.inertia_)

#%%
plt.plot(range(2, 10), inertias)

#%%
km = KMeans(n_clusters=4, random_state=42)
preds = km.fit_predict(subset_encoded)

subset_encoded.groupby(preds).mean().style.background_gradient(cmap='coolwarm', axis=0)

