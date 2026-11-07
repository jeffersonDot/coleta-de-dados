import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

tabelas = pd.read_html(html)

print(tabelas[0].head(30))