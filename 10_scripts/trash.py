# %%
import matplotlib
import pandas as pd
import numpy as np
import pyreadstat
import os
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# %%
# read in the data
# pd.set_option("display.max_rows", 100, "display.max_columns", 100)
df1 = pd.read_parquet("../20_intermediate_files/W1focusdata.parquet")
df2 = pd.read_parquet("../20_intermediate_files/W2focusdata.parquet")

#%%
import matplotlib.pyplot as plt
import seaborn as sns

#%%
fig, ax = plt.subplots(figsize=(20, 4))
sns.heatmap(df1.groupby("country").apply(lambda x: x.isna().mean()), ax=ax)

#%%
fig, ax = plt.subplots(figsize=(20, 10))
consideration_set = df1["country"].unique().tolist()
df2 = df2.loc[df2["country"].isin(consideration_set)]
df2["country"] = df2["country"].cat.remove_unused_categories()
sns.heatmap(df2.groupby("country").apply(lambda x: x.isna().mean()))

#%%
# variables to drop for W2
["language", "generations", "q42"]

#%%
w2_to_drop_per_country = {
    "Hong Kong": ["q142", "q144", "q118", "q82", "q80", "q18"],
    "Korea": ["q80", "q59", "q42", "q18"],
    "Mainland China": ["q18", "q42", "q54", "q80", "q83", "q99"],
}

#%%
#
# df2.query("country == 'Mainland China'")[['q38', 'q41', 'q40']].value_counts()
print(f"""{df2.query("country == 'Mainland China'")['q38'].value_counts()}""")
print(f"""{df2.query("country == 'Mainland China'")['q40'].value_counts()}""")
print(f"""{df2.query("country == 'Mainland China'")['q41'].value_counts()}""")

#%%
# pd.crosstab(df2.query("country == 'Mainland China'")['q41'].isna(), df2.query("country == 'Mainland China'")['q40'].isna())

#%%
s1 = set(df1["country"].unique())
s2 = set(df2["country"].unique())

list(s2.difference(s1))

#%%


#%%

pseudo_na = [
    "Can’t choose",
    "Decline to answer",
    "No answer",
    "Do not understand the question",
]

df2[df2.isin(pseudo_na)] = np.nan


#%%
print(df2.query("country == 'Mainland China'")["q18"].value_counts())
print(df2.query("country == 'Mainland China'")["q18"].isna().sum())


#%%
print(df2.query("country == 'Mainland China'")["income_quintile"].value_counts())
print(df2.query("country == 'Mainland China'")["income_quintile"].isna().sum())

#%%
for relig in df1["religion"].unique():
    print(relig)

religion_w1w2_mapper = {
    "None": "None",
    "Buddhist": "Buddhism",
    "Protestant": "Protestantism",
    "Islam": "Islam",
    "Sunni": "Islam",
    "Shia": "Islam",
    "Other": "Others",
    "Roman Catholic": "Roman Catholics",
    "Taoism": "Daoism",
    "nan": "nan",
    "Traditional folk religion (Shenism)": "Other Folk Religio",
    "Shinto": "Shinto",
    "Born Again": "Born again",
    "": "Hinduism",
    # TODO: everything else = "Other"
}

total_dict = dict()
for religion in df2['religion'].unique():
    if religion in religion_w1w2_mapper.keys():
        total_dict[religion] = religion_w1w2_mapper[religion]
    else:
        total_dict[religion] = "Others"

print(total_dict)


#%%
df2['income_quintile'].isna().to_frame().groupby(df2['urban_rural']).mean().style.background_gradient(cmap='coolwarm')