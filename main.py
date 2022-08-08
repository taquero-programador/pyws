#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup, NavigableString

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

def by_string(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previuos_element, NavigableString))

for tag in soup.find_all(by_string):
    print(tag.name)
