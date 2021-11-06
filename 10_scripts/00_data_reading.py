#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

from data_mapping import column_mapping
from data_mapping import response_mapping

COUNTRY = "Japan"


pd.set_option("display.max_rows", 100, "display.max_columns", 100)

df, meta = pyreadstat.read_sav(
    os.path.join("../00_source_data/W1 Merged Data/Wave.1_Data/Japan/japan v4.2.sav")
)
# df.head(10)


imp_vars = pd.read_csv(
    "https://raw.githubusercontent.com/DukeUndergraduateML/datathon2021/main/important-variables/D2-ABS1%2B2.csv",
    header=1,
)
imp_cols = imp_vars[imp_vars["ABS1_Coding_name"] != "na"]["ABS1_Coding_name"].tolist()

# %%
df2 = pd.concat([df.iloc[:, :11], df[imp_cols]], axis=1)
df2.head()


#%%
for colname, unique_vals in response_mapping.items():
    df2[colname] = df2[colname].replace(unique_vals)

# %%
df2.rename(column_mapping, axis=1, inplace=True)

# %%
cat_cols = [
    "country",
    "area",
    "urban_rural",
    "grtokyo50",
    "grkansai30",
    "citysize",
    "gender",
    "maritalstatus",
    "education",
    "income",
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

int_cols = [
    "yrsurvey",
    "month",
    "day",
    "time",
    "age"
]


#%%

df2 = df2.drop("country", axis=1)
df2['country'] = COUNTRY

for catcol in cat_cols:
    df2[catcol] = df2[catcol].astype("category")

for intcol in int_cols:
    df2[intcol] = df2[intcol].astype("int")

# %%
