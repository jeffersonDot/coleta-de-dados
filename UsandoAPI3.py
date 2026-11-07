import requests
import pandas as pd

dados = requests.get(
    "https://jsonplaceholder.typicode.com/users"
).json()

df = pd.DataFrame(dados)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

print("Colunas encontradas:")
print(df.columns.tolist())

print("Linhas encontradas: ")
print(df.index.tolist())

print(f"Total de linhas: {len(df)}")

print("\nPrimeiras linhas:")
print(df.head())
