import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("postgresql://cosmiuri@localhost:5432/exoplanets_db")
df = pd.read_sql("SELECT * FROM clean_exoplanets_filtered", engine)

df['density'] = df['pl_bmasse'] / df['pl_rade']

# Index(['pl_name', 'pl_bmasse', 'pl_rade', 'pl_orbper', 'st_teff', 'st_mass'], dtype='str')

df["log_mass"] = np.log(df["pl_bmasse"])
df["log_radius"] = np.log(df["pl_rade"])
df["log_orbital_period"] = np.log(df["pl_orbper"])

# star scaling (optional)
df["temp_scaled"] = df["st_teff"] / 5778  # relative to Sun

print(df.head())
print("\nColumns:\n", df.columns)