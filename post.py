#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')

lista = []
for list_ in soup.find_all('td'):
    title = list_.a
    if title == None:
        continue
    if not title.text.startswith(' '):
        lista.append(title.text)

    year = list_.find('span', class_='secondaryInfo')
    if year == None:
        continue
    lista.append(year.text.replace('(', '').replace(')', ''))

    raiting

print(len(lista))
