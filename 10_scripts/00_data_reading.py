#%%
import pandas as pd
import numpy as np
import pyreadstat
import os

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

# %%
# Subsetting meta dictionary woth important columns


#%%

column_rename = {
    "country": "country",
    "idnumber": "idnumber",
    "level1": "area",
    "level3": "urban-rural",
    "grtokyo": "grtokyo50",
    "grkansai": "grkansai30",
    "jcity": "citysize",
    "yrsurvey": "yrsurvey",
    "month": "month",
    "day": "day",
    "time": "time",
    "se002": "gender",
    "se004": "maritalstatus",
    "se005": "education",
    "se009": "income",
    "se003a": "age",
    "q007": "q007",
    "q008": "q008",
    "q009": "q009",
    "q010": "q010",
    "q006": "q006",
    "q098": "q098",
    "q128": "q128",
    "q005": "q005",
    "q027": "q027",
    "q028": "q028",
    "q105": "q105",
    "q106": "q106",
    "q121": "q121",
    "q123": "q123",
    "q127": "q127",
}

df2.rename(column_rename, axis=1, inplace=True)

new_dict = {
    "country": {1.0: "Japan"},
    "yrsurvey": {2003.0: "2003"},
    "month": {1.0: "1", 2.0: "2"},
    "day": {
        1.0: "1",
        2.0: "2",
        3.0: "3",
        4.0: "4",
        22.0: "22",
        23.0: "23",
        24.0: "24",
        25.0: "25",
        26.0: "26",
        27.0: "27",
        28.0: "28",
        29.0: "29",
        30.0: "30",
        31.0: "31",
    },
    "time": {
        15.0: "15",
        18.0: "18",
        19.0: "19",
        20.0: "20",
        21.0: "21",
        22.0: "22",
        23.0: "23",
        24.0: "24",
        25.0: "25",
        26.0: "26",
        27.0: "27",
        28.0: "28",
        29.0: "29",
        30.0: "30",
        31.0: "31",
        32.0: "32",
        33.0: "33",
        34.0: "34",
        35.0: "35",
        36.0: "36",
        37.0: "37",
        38.0: "38",
        39.0: "39",
        40.0: "40",
        41.0: "41",
        42.0: "42",
        43.0: "43",
        44.0: "44",
        45.0: "45",
        46.0: "46",
        47.0: "47",
        48.0: "48",
        49.0: "49",
        50.0: "50",
        51.0: "51",
        52.0: "52",
        53.0: "53",
        54.0: "54",
        55.0: "55",
        56.0: "56",
        57.0: "57",
        58.0: "58",
        60.0: "60",
        63.0: "63",
        65.0: "65",
        67.0: "67",
        70.0: "70",
        72.0: "72",
        74.0: "74",
        75.0: "75",
        80.0: "80",
        85.0: "85",
        90.0: "90",
        95.0: "95",
        100.0: "100",
        107.0: "107",
    },
    "q005": {
        1.0: "Much worse now",
        2.0: "A little worse now",
        3.0: "About the same",
        4.0: "A little better now",
        5.0: "Much better now",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q006": {
        1.0: "Much Worse",
        2.0: "A little Worse",
        3.0: "About the same",
        4.0: "A little Better",
        5.0: "Much Better",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q007": {
        1.0: "None at all",
        2.0: "Not very much trust",
        3.0: "Quite a lot of trust",
        4.0: "A great deal of trust",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "q008": {
        1.0: "None at all",
        2.0: "Not very much trust",
        3.0: "Quite a lot of trust",
        4.0: "A great deal of trust",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "q009": {
        1.0: "None at all",
        2.0: "Not very much trust",
        3.0: "Quite a lot of trust",
        4.0: "A great deal of trust",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "q010": {
        1.0: "None at all",
        2.0: "Not very much trust",
        3.0: "Quite a lot of trust",
        4.0: "A great deal of trust",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "q027": {
        1.0: "No",
        2.0: "Yes",
        97.0: "was under voting age",
        98.0: "Don't remember",
        99.0: "No answer",
    },
    "q028": {
        96.0: "Forgot",
        97.0: "was under voting age",
        98.0: "Don't know",
        99.0: "No answer",
        101.0: "LDP",
        102.0: "DPJ",
        103.0: "New Komeito",
        104.0: "SDP",
        105.0: "JCP",
        106.0: "NCP",
        107.0: "LP",
        108.0: "Other parties",
        109.0: "Not affiliated",
    },
    "q098": {
        1.0: "Not at all satisfied",
        2.0: "Not very satisfied",
        3.0: "Fairly satisfied",
        4.0: "Very satisfied",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q105": {
        1.0: "Much worse",
        2.0: "Somewhat worse",
        3.0: "Much the same",
        4.0: "Somewhat better",
        5.0: "Much better than before",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q106": {
        1.0: "Much worse",
        2.0: "Somewhat worse",
        3.0: "Much the same",
        4.0: "Somewhat better",
        5.0: "Much better than before",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q121": {
        1.0: "Strongly agree",
        2.0: "Somewhat agree",
        3.0: "Somewhat disagree",
        4.0: "Strongly disagree",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q123": {
        1.0: "Strongly agree",
        2.0: "Somewhat agree",
        3.0: "Somewhat disagree",
        4.0: "Strongly disagree",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q127": {
        1.0: "Strongly agree",
        2.0: "Somewhat agree",
        3.0: "Somewhat disagree",
        4.0: "Strongly disagree",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q128": {
        1.0: "Strongly agree",
        2.0: "Somewhat agree",
        3.0: "Somewhat disagree",
        4.0: "Strongly disagree",
        98.0: "Don't know",
        99.0: "No answer",
    },
}

#%%
for colname, unique_vals in new_dict.items():
    df2[colname] = df2[colname].replace(unique_vals)
