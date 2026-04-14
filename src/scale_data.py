import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler

engine = create_engine("postgresql://cosmiuri@localhost:5432/exoplanets_db")

query = "select * from clean_exoplanets"
df = pd.read_sql(query, engine)

X = df.drop(columns=["pl_name"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X.head())
print(X_scaled[:5])