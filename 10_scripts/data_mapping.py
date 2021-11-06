column_mapping = {
    "country": "country",
    "idnumber": "idnumber",
    "level1": "area",
    "level3": "urban_rural",
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

response_mapping = {
    "country": {1.0: "Japan"},
    "level3": {1.0: "urban", 2.0: "rural"},
    "grtokyo": {1.0: "yes, within", 2.0: "no"},
    "grkansai": {1.0: "yes, within", 2.0: "no"},
    "jcity": {
        1.0: "Metropolis (MT million)",
        2.0: "Cities MT 200T",
        3.0: "MT 100T",
        4.0: "LT 100T",
        5.0: "Towns & Villages",
    },
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
    "se002": {1.0: "male", 2.0: "female"},
    "se003a": {
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
        59.0: "59",
        60.0: "60",
        61.0: "61",
        62.0: "62",
        63.0: "63",
        64.0: "64",
        65.0: "65",
        66.0: "66",
        67.0: "67",
        68.0: "68",
        69.0: "69",
        70.0: "70",
        71.0: "71",
        72.0: "72",
        73.0: "73",
        74.0: "74",
        75.0: "75",
        76.0: "76",
        77.0: "77",
        78.0: "78",
        79.0: "79",
        80.0: "80",
        81.0: "81",
        82.0: "82",
        83.0: "83",
        84.0: "84",
        85.0: "85",
        86.0: "86",
        87.0: "87",
        88.0: "88",
        90.0: "90",
        93.0: "93",
    },
    "se004": {
        1.0: " Married",
        2.0: "Living-in as married",
        3.0: "Widowed",
        4.0: "Separated",
        5.0: "Divorced",
        6.0: "Single_Never married",
        98.0: "Don't know",
    },
    "se005": {
        2.0: "Incomplete elementary school",
        3.0: "Complete elementary school",
        4.0: "Incomplete secondary school",
        5.0: "Complete secondary school",
        6.0: "Incomplete high school",
        7.0: "Complete high school",
        8.0: "Some university_college education",
        9.0: "University_college degree",
        10.0: "Post graduate degree",
        98.0: "Don't know",
    },
    "se009": {
        1.0: "Less than 2,500,000 yen",
        2.0: "GE 2,500,000 LT 4,500,000 yen",
        3.0: "GE 4,500,000 LT 6,500,000 yen",
        4.0: "GE 6,500,000 LT 10,000,000 yen",
        5.0: "GE 10,000,000 yen",
        98.0: "don't know",
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


merge_column_mapping = {
    "se003": "agegroup",
    "se004a": "married",
    "se005a": "educyear",
    "level3": "urban_rural",
    "se002": "gender",
    "se003a": "age",
    "se004": "maritalstatus",
    "se004a": "married",
    "se005": "education",
    "se005a": "educationyear",
    "se009": "income_quantile",
}


merge_response_mapping = {
    "country": {
        1.0: "Japan",
        2.0: "Hong Kong",
        3.0: "Korea",
        4.0: "Mainland China",
        5.0: "Mongolia",
        6.0: "Philippines",
        7.0: "Taiwan",
        8.0: "Thailand",
    },
    "level3": {1.0: "urban", 2.0: "rural", 3.0: "no registration"},
    "yrsurvey": {2001.0: "2001", 2002.0: "2002", 2003.0: "2003"},
    "se002": {1.0: "male", 2.0: "female", 99.0: "No Answer"},
    "se003": {
        1.0: "18-19",
        2.0: "20-24",
        3.0: "25-29",
        4.0: "30-34",
        5.0: "35-39",
        6.0: "40-44",
        7.0: "45-49",
        8.0: "50-54",
        9.0: "55-59",
        10.0: "60-70",
        11.0: "71-75",
        12.0: "76 & over",
        99.0: "No Answer",
    },
    "se003a": {
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
        59.0: "59",
        60.0: "60",
        61.0: "61",
        62.0: "62",
        63.0: "63",
        64.0: "64",
        65.0: "65",
        66.0: "66",
        67.0: "67",
        68.0: "68",
        69.0: "69",
        70.0: "70",
        71.0: "71",
        72.0: "72",
        73.0: "73",
        74.0: "74",
        75.0: "75",
        76.0: "76",
        77.0: "77",
        78.0: "78",
        79.0: "79",
        80.0: "80",
        81.0: "81",
        82.0: "82",
        83.0: "83",
        84.0: "84",
        85.0: "85",
        86.0: "86",
        87.0: "87",
        88.0: "88",
        89.0: "89",
        90.0: "90",
        93.0: "93",
        109.0: "109",
        999.0: "No Answer",
    },
    "se004": {
        1.0: " Married",
        2.0: "Living-in as married",
        3.0: "Widowed",
        4.0: "Separated",
        5.0: "Divorced",
        6.0: "Single_Never married",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "se004a": {1.0: "Yes", 2.0: "No", 98.0: "Don't Know", 99.0: "No Answer"},
    "se005": {
        1.0: "No formal education",
        2.0: "Incomplete elementary school",
        3.0: "Complete elementary school",
        4.0: "Incomplete secondary school",
        5.0: "Complete secondary school",
        6.0: "Incomplete high school",
        7.0: "Complete high school",
        8.0: "Some university_college education",
        9.0: "University_college degree",
        10.0: "Post graduate degree",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "se005a": {
        0.0: "less than 1 year",
        1.0: "1 years",
        2.0: "2 years",
        3.0: "3 years",
        4.0: "4 years",
        5.0: "5 years",
        6.0: "6 years",
        7.0: "7 years",
        8.0: "8 years",
        9.0: "9 years",
        10.0: "10 years",
        11.0: "11 years",
        12.0: "12 years",
        13.0: "13 years",
        14.0: "14 years",
        15.0: "15 years",
        16.0: "16 years",
        17.0: "17 years",
        18.0: "18 years",
        19.0: "19 years",
        20.0: "20 years",
        21.0: "21 years",
        22.0: "22 years",
        23.0: "23 years",
        24.0: "24 years",
        25.0: "25 years",
        30.0: "30 years",
        44.0: "44 years",
        97.0: "Not applicable",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "se009": {
        1.0: "lowest quintile",
        2.0: "2nd quintile",
        3.0: "3rd quintile",
        4.0: "4th quintile",
        5.0: "5th quintile",
        97.0: "Not applicable",
        98.0: "Don't Know",
        99.0: "No Answer",
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
        0.0: "Not sure",
        1.0: "None at all",
        2.0: "Not very much trust",
        3.0: "Quite a lot of trust",
        4.0: "A great deal of trust",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "q008": {
        0.0: "Not sure",
        1.0: "None at all",
        2.0: "Not very much trust",
        3.0: "Quite a lot of trust",
        4.0: "A great deal of trust",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "q009": {
        0.0: "Not sure",
        1.0: "None at all",
        2.0: "Not very much trust",
        3.0: "Quite a lot of trust",
        4.0: "A great deal of trust",
        98.0: "Don't know",
        99.0: "No Answer",
    },
    "q010": {
        0.0: "Not sure",
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
        97.0: "Not applicable",
        98.0: "Don't remember",
        99.0: "No answer",
    },
    "q028": {
        96.0: "Forgot",
        97.0: "Not applicable",
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
        301.0: "Lee Hoi-chang",
        302.0: "Roh Moo-hyun",
        303.0: "Kwon Young-ghil",
        304.0: "Jang Se-Dong",
        501.0: "MAHN",
        502.0: "AN",
        503.0: "MAShSN",
        504.0: "IZ-BNN",
        505.0: "other",
        701.0: "James Chu Yu Soong",
        702.0: "Chan Lien",
        703.0: "Ao Lee",
        704.0: "Hsin-liang Hsu",
        705.0: "Shui-bian Chen",
        801.0: "Democrat",
        805.0: "New Aspiration",
        807.0: "Thai Rak Thai",
        809.0: "Chat Thai",
        811.0: "Thai Motherland",
        813.0: "Rassadorn",
        815.0: "Seritham",
        818.0: "Prachakorn Thai",
        821.0: "Chat Pattana",
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
        97.0: "Not Applicable",
        98.0: "Don't know",
        99.0: "No answer",
    },
    "q106": {
        1.0: "Much worse",
        2.0: "Somewhat worse",
        3.0: "Much the same",
        4.0: "Somewhat better",
        5.0: "Much better than before",
        97.0: "Not Applicable",
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
