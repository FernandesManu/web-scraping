import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

#passando o atributo e o valor direto daquele atributo
todas_frases = dados_pagina.find_all('span', itemprop="text")

for div in todas_frases:
    print(div.text)
