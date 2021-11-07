#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans
import matplotlib_inline

matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

#%%
df = pd.read_parquet("../20_intermediate_files/W1mergeddata.parquet")

#%%
q_cols = [col for col in df.columns if col.startswith("q")]
kick_out = ["q027", "q028"]

#%%
subset = df[(col for col in q_cols if col not in kick_out)].copy()

#%%
for col in subset.columns:
    subset[col] = subset[col].cat.add_categories(["missing"])
    subset[col] = subset[col].fillna("missing")


#%%

from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder()
subset_encoded = oe.fit_transform(subset)
subset_encoded = pd.DataFrame(subset_encoded, columns=subset.columns)

#%%
from sklearn.decomposition import FactorAnalysis, PCA

logliks = []
for ncomp in range(2, 10):
    fa = PCA(n_components=ncomp)
    fa.fit(subset_encoded)
    logliks.append(fa.explained_variance_ratio_.sum())

import numpy as np

plt.plot(range(2, 10), logliks)


#%%
# fa = FactorAnalysis(n_components=4, rotation="varimax")
fa = FactorAnalysis(n_components=4)
preds = fa.fit_transform(subset_encoded)

#%%
factor_names = [
    "Trusty Gov Supporters",
    "Past Satviks",
    "Not Free, Not equal :(",
    "Economic Optimists",
]
fig, ax = plt.subplots(figsize=(10, 2))
sns.heatmap(
    pd.DataFrame(fa.components_, columns=subset_encoded.columns),
    annot=True,
    yticklabels=factor_names,
    ax=ax,
)

#%%
FACTOR_TO_PREDICT = 0
y = fa.transform(subset_encoded)[:, FACTOR_TO_PREDICT]

#%%
for col in df.select_dtypes("category").columns:
    df[col] = df[col].cat.add_categories(["missing"])
    df[col] = df[col].fillna("missing")

#%%
cat_cols = df.select_dtypes("category").columns
# cols_to_ohe = [col for col in subset.columns if df[col].nunique() > 2 and col in cat_cols]
cols_to_ohe = cat_cols
#%%
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(df, y, test_size=0.3, random_state=42)

#%%

_oe_obj = None
_scaler_obj = None
_imputer_obj = None


def start_pipeline(data: pd.DataFrame):
    return data.copy()


def ordinal_encode(data: pd.DataFrame, columns, refit):
    global _oe_obj
    if refit:
        _oe_obj = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
        _oe_obj.fit(data[columns])
    data[columns] = _oe_obj.transform(data[columns])
    return data


def scale_numeric(data: pd.DataFrame, columns, refit):
    global _scaler_obj
    if refit:
        _scaler_obj = MinMaxScaler()
        _scaler_obj.fit(data[columns])
    data[columns] = _scaler_obj.transform(data[columns])
    return data


def simple_impute_numeric(data: pd.DataFrame, columns, refit):
    global _imputer_obj
    if refit:
        _imputer_obj = SimpleImputer()
        _imputer_obj.fit(data[columns])
    data[columns] = _imputer_obj.transform(data[columns])
    return data


def drop_useless_cols(data: pd.DataFrame, to_drop):
    data.drop(to_drop, axis=1, inplace=True)
    return data


#%%

xtrain = (
    xtrain.pipe(start_pipeline)
    .pipe(ordinal_encode, cols_to_ohe, refit=True)
    .pipe(scale_numeric, ["age", "educationyear"], refit=True)
    .pipe(simple_impute_numeric, ["age", "educationyear"], refit=True)
    .pipe(drop_useless_cols, ["yrsurvey"])
)

xtest = (
    xtest.pipe(start_pipeline)
    .pipe(ordinal_encode, cols_to_ohe, refit=False)
    .pipe(scale_numeric, ["age", "educationyear"], refit=False)
    .pipe(simple_impute_numeric, ["age", "educationyear"], refit=False)
    .pipe(drop_useless_cols, ["yrsurvey"])
)

#%%
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

lr = LinearRegression()
lr.fit(xtrain, ytrain)
preds = lr.predict(xtest)

#%%
dt = DecisionTreeRegressor()
dt.fit(xtrain, ytrain)
preds = dt.predict(xtest)

#%%
from lightgbm import LGBMRegressor
lgbm = LGBMRegressor(n_estimators=200)
lgbm.fit(xtrain, ytrain)
preds = lgbm.predict(xtest)

#%%
sns.jointplot(x=ytest, y=preds, kind="hex")
