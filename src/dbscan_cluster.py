import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np

# load
engine = create_engine("postgresql://cosmiuri@localhost:5432/exoplanets_db")
df = pd.read_sql("SELECT * FROM clean_exoplanets_filtered", engine)

# features
X = df.drop(columns=["pl_name"])

# --- Feature engineering ---
df["density"] = df["pl_bmasse"] / (df["pl_rade"] ** 3)

df["log_mass"] = np.log(df["pl_bmasse"])
df["log_radius"] = np.log(df["pl_rade"])
df["log_orbital_period"] = np.log(df["pl_orbper"])

df["temp_scaled"] = df["st_teff"] / 5778

# use ONLY engineered features
X = df[[
    "log_mass",
    "log_radius",
    "log_orbital_period",
    "density",
    "temp_scaled"
]]

# scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

df["cluster"] = labels

# PCA (reduce to 2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


df["cluster"] = labels

print(df.head())
print("\nCluster counts:\n", df["cluster"].value_counts().sort_index())

# plot
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
plt.title("DBSCAN Clusters (PCA projection)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()