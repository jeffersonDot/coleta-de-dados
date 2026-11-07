import requests

cep = "08535340"

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

dados = response.json()

print(dados)

