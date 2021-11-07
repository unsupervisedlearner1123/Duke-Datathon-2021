#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

df = pd.read_parquet(os.path.join("../20_intermediate_files/W1mergeddata.parquet"))

# %%
todrop = [x for x in df.columns if x.startswith("q")]
df = df.drop(todrop, axis=1)
# %%

df1, meta = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W1 Merged Data/Wave.1_Data/Merge/Wave1_20170906.sav"
    )
)

