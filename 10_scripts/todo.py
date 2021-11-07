# countries in w2 that are not in w1
["Cambodia", "Malaysia", "Indonesia", "Singapore", "Vietnam"]


########## W2 ##########
w2_to_drop_per_country = {
    "Hong Kong": ["q142", "q144", "q118", "q82", "q80", "q18"],
    "Korea": ["q80", "q59", "q42", "q18"],
    "Mainland China": ["q18", "q42", "q54", "q80", "q83", "q99"],
}

w1_vars_to_drop = [
    "language",
    "generations",
    "maritalstatus",
    "num_formal_group",
    "religion2",
    "q031",
]
w2_vars_to_drop = ["language", "generations", "q42", "maritalstatus", "num_formal_group"]
# TODO: create "married" variable in W2

religion_w1w2_mapper = {
    "None": "None",
    "Buddhist": "Buddhism",
    "Roman Catholic": "Roman Catholics",
    "Shinto": "Shinto",
    "Cannot choose": "Others",
    "Other": "Others",
    # np.nan: np.nan
    "Protestant": "Protestantism",
    "Traditional folk religion (Shenism)": "Other Folk Religio",
    "Taoism": "Daoism",
    "Other Asian religions": "Others",
    "Islam": "Islam",
    "Iglesia Ni Cristo": "Others",
    "Baptist": "Others",
    "Aglipayan": "Others",
    "Jehovah Witness": "Others",
    "Born Again": "Born again",
    "Dating Daan": "Others",
    "Seventh Day Adventist": "Others",
    "Evangelical": "Others",
    "Methodist": "Others",
    "Mormons": "Others",
    "Anglican": "Others",
    "Pentecostal": "Others",
    "Grace Gospel of Church": "Others",
    "Epescopal": "Others",
    "Tiruray": "Others",
    "I-Kuan Tao": "Others",
    "Sunni": "Islam",
    "Shia": "Islam",
}

