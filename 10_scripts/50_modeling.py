#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans
import matplotlib_inline
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, MinMaxScaler
from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.impute import SimpleImputer, KNNImputer
from data_focus import q1num_to_custom, custom_to_q1_text

matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

#%%


#%%
COUNTRY = "Taiwan"
df = pd.read_parquet(f"../20_intermediate_files/W1_countries/{COUNTRY}.parquet")

#%%
q_cols = [col for col in df.columns if col.startswith("q")]


#%%
from ordinal_orders import var_to_order_mapper
df
var_to_order_mapper_qoi = {q1num_to_custom.get(k, k): v for k, v in var_to_order_mapper.items()}

# for k, v in var_to_order_mapper.items():
#     print(k, q1num_to_custom.get(k, k), v)

# Setting the order
for var, order in var_to_order_mapper_qoi.items():
    df[var] = df[var].cat.reorder_categories(order)
subset = df[q_cols].copy()

#%%


# oe = OrdinalEncoder()
# subset_encoded = oe.fit_transform(subset)
# subset_encoded = pd.DataFrame(subset_encoded, columns=subset.columns)

# #%%

# logliks = []
# for ncomp in range(2, 10):
#     fa = PCA(n_components=ncomp)
#     fa.fit(subset_encoded)
#     logliks.append(fa.explained_variance_ratio_.sum())

# import numpy as np

# plt.plot(range(2, 10), logliks)


#%%
cat_cols = subset.select_dtypes("category").columns
float_cols = subset.select_dtypes("float").columns
# cols_to_ohe = [col for col in subset.columns if df[col].nunique() > 2 and col in cat_cols]
cols_to_ohe = cat_cols
#%%

#%%

_cat_encoder = None
# _scaler_obj = None
_imputer_obj = None


def start_pipeline(data: pd.DataFrame):
    return data.copy()


# def encode_categoricals(data: pd.DataFrame, columns, refit):
#     global _cat_encoder
#     if refit:
#         _cat_encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
#         # _cat_encoder = OneHotEncoder(handle_unknown="ignore")
#         _cat_encoder.fit(data[columns])
#     data[columns] = _cat_encoder.transform(data[columns])  # Ordinal Encode
#     return data


def encode_categoricals(data: pd.DataFrame, columns, refit):
    for catcol in columns:
        data[catcol] = data[catcol].cat.codes
    return data


def scale_numeric(data: pd.DataFrame, columns, refit):
    global _scaler_obj
    if refit:
        _scaler_obj = MinMaxScaler()
        _scaler_obj.fit(data[columns])
    data[columns] = _scaler_obj.transform(data[columns])
    return data


def simple_impute_numeric(data: pd.DataFrame, columns, refit, na_value):
    global _imputer_obj
    if refit:
        _imputer_obj = KNNImputer(missing_values=na_value, n_neighbors=5)
        # _imputer_obj.fit(data[columns])
        _imputer_obj.fit(data)
        # print("FITTED!")
    # data[columns] = _imputer_obj.transform(data[columns])
    _colnames = data.columns
    data = _imputer_obj.transform(data)
    return pd.DataFrame(data, columns=_colnames)


# def drop_useless_cols(data: pd.DataFrame, to_drop):
#     data.drop(to_drop, axis=1, inplace=True)
#     return data


#%%
subset_encoded = (
    subset.pipe(start_pipeline)  # pd.get_dummies(subset, drop_first=True)
    .pipe(encode_categoricals, columns=cols_to_ohe, refit=True)
    .pipe(simple_impute_numeric, float_cols, True, na_value=np.nan)
    .pipe(simple_impute_numeric, cat_cols, True, na_value=-1)
    .pipe(scale_numeric, float_cols, True)
)

subset_encoded = subset_encoded.drop("qoi029", axis=1)
# subset_encoded.to_parquet(f"../20_intermediate_files/W1_countries/qcols_encoded_{COUNTRY}.parquet")

#%%

# evrs = []
# for ncomp in range(2, 25):
#     pca = PCA(n_components=ncomp)
#     pca.fit(subset_encoded)
#     evrs.append(pca.explained_variance_ratio_.sum())

# plt.plot(range(2, 25), evrs)

pca = PCA(n_components=59)
pca.fit(subset_encoded)
plt.plot(pca.explained_variance_ratio_[:15])

#%%
# fa = FactorAnalysis(n_components=4, rotation="varimax")
fa = FactorAnalysis(n_components=3)
preds = fa.fit_transform(subset_encoded)

#%%


fig, ax = plt.subplots(figsize=(15, 2))
sns.heatmap(
    pd.DataFrame(fa.components_, columns=subset_encoded.columns),
    # annot=True,
    ax=ax,
)


#%%
FACTOR_TO_PREDICT = 0
y = fa.transform(subset_encoded)[:, FACTOR_TO_PREDICT]

#%%
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

predictors = [
    # "country",
    "urban_rural",
    "gender",
    "agegroup",
    "married",
    "education",
    "income_quintile",
    "religion",
    "socialstatus",
]
xtrain, xtest, ytrain, ytest = train_test_split(df[predictors], y, test_size=0.3, random_state=42)

xtrain = (
    xtrain.pipe(start_pipeline)
    .pipe(encode_categoricals, columns=predictors, refit=True)
    .pipe(simple_impute_numeric, predictors, True, na_value=-1)
)

xtest = (
    xtest.pipe(start_pipeline)
    .pipe(encode_categoricals, columns=predictors, refit=False)
    .pipe(simple_impute_numeric, predictors, False, na_value=-1)
)


#%%
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

# lr = LinearRegression()
# lr.fit(xtrain, ytrain)
# preds = lr.predict(xtest)

# #%%
# dt = DecisionTreeRegressor()
# dt.fit(xtrain, ytrain)
# preds = dt.predict(xtest)

# #%%
# from lightgbm import LGBMRegressor

# lgbm = LGBMRegressor(n_estimators=200)
# lgbm.fit(xtrain, ytrain)
# preds = lgbm.predict(xtest)

#%%
sns.jointplot(x=ytest, y=preds, kind="hex")
