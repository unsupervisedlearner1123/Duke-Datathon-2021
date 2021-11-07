import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_parquet(
    os.path.join("./20_intermediate_files/W1_countries/ALLCOUNTRIES.parquet")
)

# cols_list = [x for x in df.columns if x.startswith("q")]

# cols_list.append("country")
# fig, ax = plt.subplots(figsize = (15,10))

fig = sns.catplot(
    x="qoi006",
    order=["Very Bad", "Bad", "So so", "Good", "Very Good"],
    hue="country",
    kind="count",
    data=df,
    palette="rocket",
)
fig.axes[0, 0].set_xlabel(
    "How would you rate the overall economic condition of our country today?"
)
# fig.add_legend(loc = "lower center")

fig = sns.catplot(x="qoi011", hue="country", kind="count", data=df, palette="rocket")
fig.axes[0, 0].set_xlabel(
    "What do you think the economic situation of your family will be five years from now?"
)

fig = sns.catplot(x="qoi043", hue="country", kind="count", data=df, palette="rocket")
fig.axes[0, 0].set_xlabel(
    "How satisfied or dissatisfied are you with the current government?"
)
