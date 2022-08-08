#!/usr/bin/env python3

from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
print(rel_soup.a['rel'])

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
print(rel_soup.a)
print(rel_soup.a['rel'])
