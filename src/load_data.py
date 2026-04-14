import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://cosmiuri@localhost:5432/exoplanets_db')

query = "select * from clean_exoplanets"
df = pd.read_sql(query, con=engine)

print(df.head())
print(df.shape)