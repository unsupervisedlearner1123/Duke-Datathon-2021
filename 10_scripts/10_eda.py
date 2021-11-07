#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_parquet("../20_intermediate_files/W1mergeddata.parquet")


#%%
# NA by country x variable
sns.set_context("talk")
fig, ax = plt.subplots(figsize=(15, 5))
sns.heatmap(df.groupby("country").apply(lambda g: g.isna().mean()).T)

#%%
# Marital stuff
pd.crosstab(df.married, df.maritalstatus)

#%%
# n for Age group by country
pd.pivot_table(data=df, index="agegroup", columns="country", aggfunc="size")


#%%
# Education for missing educationyear
df.education[df.educationyear.isna()].value_counts()

#%%
