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

# %%
# pick out the important columns
df = pd.concat([df1.iloc[:, :11], df1[imp_cols]], axis=1,)

# %%
# rename categories and column names
for colname, unique_vals in w2_response_mapping.items():
    df[colname] = df[colname].replace(unique_vals)

# %%
df.rename(w2_column_mapping, axis=1, inplace=True)






# %%