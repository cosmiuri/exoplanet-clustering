import requests
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine

URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

query = """
select pl_name, pl_bmasse, pl_rade, pl_orbper, st_teff, st_mass
from ps
where pl_bmasse is not null
"""

params = {
    "query": query,
    "format": "csv"
}

response = requests.get(URL, params=params)

df = pd.read_csv(StringIO(response.text))
engine = create_engine("postgresql://cosmiuri@localhost:5432/exoplanets_db")
df.to_sql("raw_exoplanets", engine, if_exists="append", index=False)


print(df.head())
print(df.shape)