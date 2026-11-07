import requests

url = "https://viacep.com.br/ws/08535340/json/"

dados = requests.get(url).json()

print("Rua: ", dados["logradouro"])
print("Cidade:", dados["localidade"])
print("Estado:", dados["uf"])
print("Bairro:", dados["bairro"])