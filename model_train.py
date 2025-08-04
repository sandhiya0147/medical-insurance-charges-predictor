import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("insurance.csv")

X = df.drop("charges", axis=1)
y = df["charges"]

categorical = ["sex", "smoker", "region"]
numeric = ["age", "bmi", "children"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), categorical)
    ], remainder='passthrough'
)

model = Pipeline(steps=[
    ('preprocessing', preprocessor),
    ('ridge', Ridge(alpha=1.0))
])

model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
