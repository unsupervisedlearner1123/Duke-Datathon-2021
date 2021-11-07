#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

from data_mapping import w2_column_mapping
from data_mapping import w2_response_mapping

# %%
# read in the data
pd.set_option("display.max_rows", 100, "display.max_columns", 100)

df1, meta = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W2 Merged Data/2w-3rd_release_all/merge/Wave2_20170724.sav"
    )
)

imp_vars = pd.read_csv(
    "https://raw.githubusercontent.com/DukeUndergraduateML/datathon2021/main/important-variables/D2-ABS1%2B2.csv",
    header=1,
)
imp_cols = imp_vars[imp_vars["ABS2_Coding_name"] != "na"]["ABS2_Coding_name"].tolist()

#%%
# remove duplicate columns
kickout = ["country", "q8", "q6", "q5"]
imp_cols = [x for x in imp_cols if x not in kickout]
addto = ["fgnum", "se6", "se8b", "se11", "se13"]
imp_cols.extend(addto)

# %%
# pick out the important columns
df = pd.concat([df1.iloc[:, :11], df1[imp_cols]], axis=1,)

#%%
# extract the data mappings
columns = dict()
for k, v in meta.column_names_to_labels.items():
    if k in df.columns:
        columns[k] = v

responses = dict()
for k, v in meta.variable_value_labels.items():
    if k in df.columns:
        responses[k] = v

# %%
# rename categories and column names
for colname, unique_vals in w2_response_mapping.items():
    df[colname] = df[colname].replace(unique_vals)

df.rename(w2_column_mapping, axis=1, inplace=True)

# %%
# drop or clean columns to change data type
df = df.drop("idnumber", axis=1)

#%%
# Factorize age to match variables from W1
df["temp"] = df["age"] == "REFUSED"
df["agegroup"] = df["age"]
df["age"] = df["age"].replace("REFUSED", np.nan).astype("float")
bins = [0, 20, 25, 30, 35, 40, 45, 50, 55, 60, 71, 76, 200]
labels = [
    "18-19",
    "20-25",
    "25-29",
    "30-34",
    "35-39",
    "40-44",
    "45-49",
    "50-54",
    "55-59",
    "60-70",
    "71-75",
    "76 & over",
]
df["agegroup"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)
df["agegroup"] = df["agegroup"].cat.add_categories("REFUSED")
df["age"] = df["age"].astype("string")
df.loc[df["temp"], "age"] = "REFUSED"
df.loc[df["temp"], "agegroup"] = "REFUSED"

#%%
# factorize social status to match variables from W1
statusmap = {
    1.0: "Lower class",
    2.0: "Lower class",
    3.0: "Lower-Middle class",
    4.0: "Lower-Middle class",
    5.0: "Middle class",
    6.0: "Middle class",
    7.0: "Upper middle class",
    8.0: "Upper middle class",
    9.0: "Upper Class",
    10.0: "Upper Class",
    97.0: "Don't understand",
    98.0: "Can't choose",
    99.0: "Decline to answer",
}
df["socialstatus"] = df["socialstatus"].map(statusmap)

#%%
# set column data types
cat_cols = [
    "country",
    "urban_rural",
    "q1",
    "q2",
    "q3",
    "q4",
    "q5",
    "q6",
    "q7",
    "q8",
    "gender",
    "maritalstatus",
    "education",
    "income_quintile",
    "num_formal_group",
    "religion",
    "generations",
    "language",
    "socialstatus",
    "q9",
    "q12",
    "q13",
    "q93",
    "q130",
    "q38",
    "q40",
    "q108",
    "q110",
    "q124",
    "q126",
    "q128",
    "q32",
    "q48",
    "q49",
    "q94",
    "q103",
    "q104",
]

for catcol in cat_cols:
    df[catcol] = df[catcol].astype("category")


# %%
# export to parquet
df.to_parquet("../20_intermediate_files/W2mergeddata.parquet")

# %%
# done :)

