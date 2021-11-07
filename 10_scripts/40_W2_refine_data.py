# %%
import pandas as pd
import numpy as np
import pyreadstat
import os
from data_focus import q2num_to_custom

# %%
# read in the data
df = pd.read_parquet("../20_intermediate_files/W2focusdata.parquet")

# %%
df = df[~df.country.isin(["Cambodia", "Malaysia", "Indonesia", "Singapore", "Vietnam"])]

#%%
# drop rows with no ordinal response as N/A for consistency with W1
replace_with_NA = [
    "Decline to answer",
    "Can’t choose",
    "No answer",
    "Do not understand the question",
    "Don't understand",
    "No answer or can't understand",
    97,
    98,
    99,
]

for rep in replace_with_NA:
    df = df.replace(rep, np.nan)

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
# create married category according to W1
df["married"] = df["maritalstatus"]
df["married"] = df["married"].map(
    {
        "Married": "Yes",
        "Widowed": "Yes",
        "Single/Never married": "No",
        "Divorced": "Yes",
        "Living-in as married": "No",
        "Separated/Married but separated/not living with legal spouse": "Yes",
    },
)

# %%
w2_vars_to_drop = [
    "language",
    "generations",
    "q42",
    "q54",
    "maritalstatus",
    "num_formal_group",
    "age",
]
df = df.drop(w2_vars_to_drop, axis=1)

# %%
w2_to_drop_per_country = {
    "Hong Kong": ["q142", "q144", "q118", "q82", "q80", "q18"],
    "Korea": ["q80", "q59", "q18"],
    "Mainland China": ["q18", "q80", "q83", "q99"],
}

#%%
df1, meta = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W2 Merged Data/2w-3rd_release_all/merge/Wave2_20170724.sav"
    )
)
#%%
ordinal_map = dict()
qs = [x for x in df.columns if x.startswith("q")]
# for q in qs:
#     ordinal_map[q] = {i:x for i,x in enumerate(meta.variable_value_labels[q].values())}
for q in qs:
    ordinal_map[q] = list(meta.variable_value_labels[q].values())



#%%
dfs = {country: df.query("country == @country") for country in df["country"].unique()}

#%%
to_rename = [x for x in df.columns if x.startswith("q")]

for countryname, dataf in dfs.items():
    print(f"Dropping cols in {countryname}")
    dataf = dataf.drop(w2_to_drop_per_country.get(countryname, []), axis=1)
    renaming = {x: q2num_to_custom[x] for x in to_rename}
    dataf = dataf.rename(columns=renaming)
    dfs[countryname] = dataf

# for countryname, dataf in dfs.items():
#     print(f"{countryname}: {dataf.shape}")
#     dataf.to_parquet(f"../20_intermediate_files/W2_countries/{countryname}.parquet")

#%%

all_to_drop = set()
for x in w2_to_drop_per_country.values():
    all_to_drop.update(set(x))
df = df.drop(all_to_drop, axis=1)
renaming = {x: q2num_to_custom[x] for x in to_rename}
df = df.rename(columns=renaming)
# df.to_parquet("../20_intermediate_files/W2_countries/ALLCOUNTRIES.parquet")

#%%
df1, meta = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W2 Merged Data/2w-3rd_release_all/merge/Wave2_20170724.sav"
    )
)
# %%
