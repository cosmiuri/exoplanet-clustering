import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

engine = create_engine("postgresql://cosmiuri@localhost:5432/exoplanets_db")
df = pd.read_sql("SELECT * FROM clean_exoplanets_filtered", engine)

X = df.drop(columns=["pl_name"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(X_scaled)

df['cluster'] = labels

print(df.head())
print("\ncluster counts: \n", df['cluster'].value_counts())

# print("\nOutlier cluster:\n")
# print(df[df["cluster"] == 2])