#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

from data_mapping import w1_column_mapping
from data_mapping import w1_response_mapping


df1, meta1 = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W1 Merged Data/Wave.1_Data/Merge/Wave1_20170906.sav"
    )
)

df2, meta2 = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W2 Merged Data/2w-3rd_release_all/merge/Wave2_20170724.sav"
    )
)
# %%

meta2.column_names_to_labels["q144"]
# %%
meta2.column_names_to_labels["fgnum"]
# %%
