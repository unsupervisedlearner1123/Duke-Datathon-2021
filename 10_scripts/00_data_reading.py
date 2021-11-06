#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

from data_mapping import column_mapping
from data_mapping import response_mapping


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
