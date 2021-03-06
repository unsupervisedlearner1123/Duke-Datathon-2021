#%%
import pandas as pd
import numpy as np
from pandas.io.parquet import to_parquet
import pyreadstat
import os
from data_focus import col_list2
from data_mapping import w2_newq_mapping

#%%
# read in existing data
df = pd.read_parquet(os.path.join("../20_intermediate_files/W2mergeddata.parquet"))

df1, meta = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W2 Merged Data/2w-3rd_release_all/merge/Wave2_20170724.sav"
    )
)
# %%
# %%
# drop explorative questions and add questions of interest
todrop = [x for x in df.columns if x.startswith("q")]
df = df.drop(todrop, axis=1)
toappend = [x for x in col_list2 if x.startswith("q")]
df = pd.concat([df, df1[toappend]], axis=1)

# %%
# find key values we need for mapping
responses = dict()
for k, v in meta.variable_value_labels.items():
    if k in toappend:
        responses[k] = v
# %%
# remap responses
for colname, unique_vals in w2_newq_mapping.items():
    df[colname] = df[colname].replace(unique_vals)

# %%
# change data types
floats = ["q95", "q96", "q97", "q98"]
toappend = [x for x in toappend if x not in floats]
df[toappend] = df[toappend].astype("category")
df[floats] = df[floats].astype("float")

# %%
# save to parquet
# df.to_parquet("../20_intermediate_files/W2focusdata.parquet")

# %%
# done :)

# %%
