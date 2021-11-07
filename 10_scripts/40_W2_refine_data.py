# %%
import pandas as pd
import numpy as np
import os
from data_focus import q2num_to_custom


##################################################################################################
################################# WHEN COMPLETE, RUN RENAME BELOW ################################
##################################################################################################

# %%
# read in the data
df = pd.read_parquet("../20_intermediate_files/W2focusdata.parquet")

# %%
df = df[~df.country.isin(["Cambodia", "Malaysia", "Indonesia", "Singapore", "Vietnam"])]

# %%
# rename religion to religion_code
religion_w1w2_mapper = {
    "None": "None",
    "Buddhist": "Buddhism",
    "Roman Catholic": "Roman Catholics",
    "Shinto": "Shinto",
    "Cannot choose": "Others",
    "Other": "Others",
    # np.nan: np.nan
    "Protestant": "Protestantism",
    "Traditional folk religion (Shenism)": "Other Folk Religio",
    "Taoism": "Daoism",
    "Other Asian religions": "Others",
    "Islam": "Islam",
    "Iglesia Ni Cristo": "Others",
    "Baptist": "Others",
    "Aglipayan": "Others",
    "Jehovah Witness": "Others",
    "Born Again": "Born again",
    "Dating Daan": "Others",
    "Seventh Day Adventist": "Others",
    "Evangelical": "Others",
    "Methodist": "Others",
    "Mormons": "Others",
    "Anglican": "Others",
    "Pentecostal": "Others",
    "Grace Gospel of Church": "Others",
    "Epescopal": "Others",
    "Tiruray": "Others",
    "I-Kuan Tao": "Others",
    "Sunni": "Islam",
    "Shia": "Islam",
}
df.religion = df.religion.map(religion_w1w2_mapper)

# %%
w2_vars_to_drop = ["language", "generations", "q42", "maritalstatus", "num_formal_group"]
df = df.drop(w2_vars_to_drop, axis=1)

# %%
w2_to_drop_per_country = {
    "Hong Kong": ["q142", "q144", "q118", "q82", "q80", "q18"],
    "Korea": ["q80", "q59", "q18"],
    "Mainland China": ["q18", "q54", "q80", "q83", "q99"],
}

#%%
dfs = {country: df.query("country == @country") for country in df['country'].unique()}

for countryname, dataf in dfs.items():
    print(f"Dropping cols in {countryname}")
    dataf = dataf.drop(w2_to_drop_per_country.get(countryname, []), axis=1)
    dfs[countryname] = dataf

#%%
for countryname, dataf in dfs.items():
    print(f"{countryname}: {dataf.shape}")
    dataf.to_parquet(f"../20_intermediate_files/W2_countries/{countryname}.parquet")

#%%

all_to_drop = set()
for x in w2_to_drop_per_country.values():
    all_to_drop.update(set(x))

df.drop(all_to_drop, axis=1).to_parquet("../20_intermediate_files/W2_countries/ALLCOUNTRIES.parquet")


######################################### RUN HERE LATER ###########################################
#%%
# to_rename = [x for x in df.columns if x.startswith("q")]
# renaming = {x:q2num_to_custom[x] for x in to_rename}
# df = df.rename(columns=renaming)
