#criando um metodo que avalia se o atributo esta dentrodos criterios 
import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

def filtro(class_css):
    return class_css is not None and len(class_css) > 4

todas_frases = dados_pagina.find_all('div', class_= filtro)

for div in todas_frases:
    print(div['class'])