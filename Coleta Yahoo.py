import pandas
import requests
from bs4 import BeautifulSoup

print ('Requests: ')
response = requests.get('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue')
print(response.text[:600])

soup = BeautifulSoup(response.text,features='html.parser')

print(soup.prettify() [:1000])

print('Pandas: ')
url_dados = pandas.read_html('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue')
print (url_dados [0].head(10))