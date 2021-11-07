# %%
import pandas as pd
import numpy as np
import pyreadstat
import os

# %%
# read in the data
pd.set_option("display.max_rows", 100, "display.max_columns", 100)

df1, meta = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W1 Merged Data/Wave.1_Data/Merge/Wave1_20170906.sav"
    )
)

df2, meta2 = pyreadstat.read_sav(
    os.path.join(
        "../00_source_data/W2 Merged Data/2w-3rd_release_all/merge/Wave2_20170724.sav"
    )
)

comp = pd.read_csv(
    "https://raw.githubusercontent.com/unsupervisedlearner1123/Duke-Datathon-2021/main/20_intermediate_files/w1_w2_mapping.txt?token=AQKRUJB4YQ6CMZVY7NXJXHTBSBIWC",
    names=["wave1", "wave2"],
    header=None,
    sep="<==>",
)

meta_filter = [
    col for col in meta.column_labels if col in comp["wave1"].str.strip().tolist()
]
col_list = [
    key for key, val in meta.column_names_to_labels.items() if val in meta_filter
]
df_wave1 = df1[col_list]

meta_filter2 = [
    col for col in meta2.column_labels if col in comp["wave2"].str.strip().tolist()
]
col_list2 = [
    key for key, val in meta2.column_names_to_labels.items() if val in meta_filter2
]
df_wave2 = df2[col_list2]