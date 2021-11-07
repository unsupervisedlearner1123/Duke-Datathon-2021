#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

from data_mapping import w1_column_mapping
from data_mapping import w1_response_mapping

# %%
# read in the data
pd.set_option("display.max_rows", 100, "display.max_columns", 100)

df1, meta = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W1 Merged Data/Wave.1_Data/Merge/Wave1_20170906.sav"
    )
)

imp_vars = pd.read_csv(
    "https://raw.githubusercontent.com/DukeUndergraduateML/datathon2021/main/important-variables/D2-ABS1%2B2.csv",
    header=1,
)
imp_cols = imp_vars[imp_vars["ABS1_Coding_name"] != "na"]["ABS1_Coding_name"].tolist()

#%%
# remove duplicate columns
kickout = ["se004", "country", "se002", "se003a", "se005"]
addto = ['se006','se008b','se014','se017','relig1','fgnum']
imp_cols = [x for x in imp_cols if x not in kickout]
imp_cols.extend(addto)

# %%
# pick out the important columns
df = pd.concat([df1.iloc[:, :11], df1[imp_cols]], axis=1,)

# %%
# rename categories and column names
for colname, unique_vals in w1_response_mapping.items():
    df[colname] = df[colname].replace(unique_vals)

df.rename(w1_column_mapping, axis=1, inplace=True)

# %%
# clean the columns for data type assignment
df = df.drop("idnumber", axis=1)

df["educationyear"] = (
    df["educationyear"]
    .replace("less than 1 year", 0)
    .astype("string")
    .str.replace(" years", "")
    .astype("float")
)
# %%
# set column data types
cat_cols = [
    "country",
    "urban_rural",
    "agegroup",
    "age",
    "maritalstatus",
    "married",
    "education",
    "gender",
    "income_quintile",
    "religion",
    "generations",
    "language",
    "socialstatus",
    "religion2",
    "num_formal_group",
    "q007",
    "q008",
    "q009",
    "q010",
    "q006",
    "q098",
    "q128",
    "q005",
    "q027",
    "q028",
    "q105",
    "q106",
    "q121",
    "q123",
    "q127",
]

fl_cols = ["yrsurvey", "age", "educationyear"]

for catcol in cat_cols:
    df[catcol] = df[catcol].astype("category")

for flcol in fl_cols:
    df[flcol] = df[flcol].astype("float")

# %%
# export to parquet
# df.to_parquet("../20_intermediate_files/W1mergeddata.parquet")
# %%
# done :)
