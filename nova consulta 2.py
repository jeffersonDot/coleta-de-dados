import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

df = pd.read_html(StringIO(html))[0]

# Mostrar todas as colunas
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("Colunas encontradas:")
print(df.columns.tolist())

print("\nPrimeiras linhas:")
print(df.head())