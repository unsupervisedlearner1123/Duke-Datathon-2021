# %%
import pandas as pd
import numpy as np
import pyreadstat
import os

# import matplotlib_inline
# matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

# %%
# read in the data
df = pd.read_parquet("../20_intermediate_files/W1focusdata.parquet")

w1_vars_to_drop = [
    "language",
    "generations",
    "maritalstatus",
    "num_formal_group",
    "religion2",
    "q031",
    "age",
]

w1_to_drop_per_country = {
    "Hong Kong": ["q115", "q077", "q057", "q017", "q013"],
    "Korea": ["q017", "q074"],
    "Mainland China": [
        "q125",
        "q121",
        "q115",
        "q104",
        "q077",
        "q074",
        "q062",
        "q057",
        "q017",
    ],
    "Taiwan": ["q057"],
}
#%%
df = df.drop(w1_vars_to_drop, axis=1)

#%%
dfs = {country: df.query("country == @country") for country in df['country'].unique()}

for countryname, dataf in dfs.items():
    print(f"Dropping cols in {countryname}")
    dataf = dataf.drop(w1_to_drop_per_country.get(countryname, []), axis=1)
    dfs[countryname] = dataf

#%%
for countryname, dataf in dfs.items():
    print(f"{countryname}: {dataf.shape}")
    dataf.to_parquet(f"../20_intermediate_files/W1_countries/{countryname}.parquet")

#%%

all_to_drop = set()
for x in w1_to_drop_per_country.values():
    all_to_drop.update(set(x))

df.drop(all_to_drop, axis=1).to_parquet("../20_intermediate_files/W1_countries/ALLCOUNTRIES.parquet")