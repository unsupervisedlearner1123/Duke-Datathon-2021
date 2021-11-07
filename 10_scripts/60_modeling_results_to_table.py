#%%
import re

countries = [
    "Hong Kong",
    "Japan",
    "Korea",
    "Mainland China",
    "Mongolia",
    "Philippines",
    "Taiwan",
    "Thailand",
]

############ W1 ############
datalist = []
for country in countries:
    with open(f"../30_results/W1/{country}.txt", "r") as f:
        lines = f.read()

    r2_pattern = re.compile(r"(?<!Adj. )R-squared:\s*(?P<r2>[01].\d+)")
    found = r2_pattern.findall(lines)

    datalist.append(
        {"country": country, "r2_f0": found[0], "r2_f1": found[1], "r2_f2": found[2],}
    )


import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(datalist)
data['country'] = data['country'].astype('category')
data[["r2_f0", "r2_f1", "r2_f2"]] = data[["r2_f0", "r2_f1", "r2_f2"]].astype('float')
data.style.background_gradient(cmap="Blues")

#%%
############ W2 ############
datalist = []
for country in countries:
    with open(f"../30_results/W2/{country}.txt", "r") as f:
        lines = f.read()

    r2_pattern = re.compile(r"(?<!Adj. )R-squared:\s*(?P<r2>[01].\d+)")
    found = r2_pattern.findall(lines)

    datalist.append(
        {"country": country, "r2_f0": found[0], "r2_f1": found[1], "r2_f2": found[2],}
    )


import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(datalist)
data['country'] = data['country'].astype('category')
data[["r2_f0", "r2_f1", "r2_f2"]] = data[["r2_f0", "r2_f1", "r2_f2"]].astype('float')
data.style.background_gradient(cmap="Blues")