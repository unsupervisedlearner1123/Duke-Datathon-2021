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
