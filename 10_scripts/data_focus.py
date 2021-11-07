# %%
import pandas as pd
import numpy as np
import pyreadstat
import os
import csv


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
    sep=" <==> ",
)

#%%
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

#%%
custom_to_q1num = {f"qoi{idx:0>3}": col_list[idx] for idx in range(1, len(col_list))}
q1num_to_custom = {val: key for key, val in custom_to_q1num.items()}

#%%
q1text_to_q1num = {v: k for k, v in meta.column_names_to_labels.items()}
q1text_to_q1num
#%%
q1num_to_q2text = {q1text_to_q1num.get(minidict["wave1"].strip()): minidict["wave2"] for minidict in comp.to_dict("records")}
q1num_to_q2text

#%%
custom_to_q2text = {q1num_to_custom.get(key): q1num_to_q2text.get(key) for key, _ in q1num_to_q2text.items()}


q2text_to_q2num = {v: k for k, v in meta2.column_names_to_labels.items()}
q2num_to_q2text = {val: key for key, val in q2text_to_q2num.items()}

#%%
custom_to_q2num = {custom: q2text_to_q2num.get(q2text) for custom, q2text in custom_to_q2text.items()}
q2num_to_custom = {val: key for key, val in custom_to_q2num.items()}

#%%
q1num_to_q1_text = {val: key for key, val in q1text_to_q1num.items()}
custom_to_q1_text = {key: q1num_to_q1_text.get(custom_to_q1num.get(key)) for key, value in custom_to_q1num.items()}
custom_to_q1_text
# %%

# import json
# with open("../20_intermediate_files/w1_questions.json", "w") as write_file:
#     json.dump(q1num_to_custom, write_file)
# %%
