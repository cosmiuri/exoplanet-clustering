import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("postgresql://cosmiuri@localhost:5432/exoplanets_db")
df = pd.read_sql("SELECT * FROM clean_exoplanets_filtered", engine)

X = df.drop(columns=['pl_name']).values

X = (X - X.mean(axis=0)) / X.std(axis=0)

k = 3
max_iters = 100

np.random.seed(42)
indices = np.random.choice(len(X), size=k, replace=False)
centroids = X[indices]

for i in range(max_iters):

    distances = np.linalg.norm(X[:,None])
