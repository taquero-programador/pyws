from bs4 import BeautifulSoup

with open("index.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(type(tag))
# convierte el html a unicode

# clases de objeto
"""
transforma un documento html compejo a un arbol de datos.
los cuatro pricipales son Tag, NavigableString, BeautifulSoup
y Comment
"""
# tag
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soub.b
print(type(tag)) # retorna el tipo

# name: cada etiqueta tiene un nombre accible tag.name
print(tag.name)
# si el nombre de la etiqueta cambia, el cambio se refleja en el html generado
tag.name = "blockqoute"
print(tag.name)
# attributes
"""
una etiqueta puede tener cualquier numero de atributos. la etiqueta <b id="boldest"> tiene un atributo id con valor "boldest".
se puede acceder a los atributos tratando las etiquetas como un diccionario"""
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser).b
print(tag['id']) # devuele el diccionario de la etiqueta

# para modificar un atributo se debe tratar como un diccionairo
tag['id'] = "verybold"
tag['another-atribute'] = 1
print(tag) # retorna toda la etiqueta
# eliminar los atributos
del tag['id']
del tag['another-atribute']
print(tag) # retorna la etiqueta sin atributos
# al querer acceder a un atributo devuelve error al no existir
print(tag['id'])
"""
Atributos de valores multiples
los atributos más comunes son class(puede tener más de una),rel, rev,
accept-charset, headers y accesskey. b4s los representa como una lista
"""
css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser').b
print(css_soup['class'])
# multiple etiqueta
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(css_soup.p['class'])
# un atributo parece tener más de un atributo pero no es así
id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print(id_soup.p['id']) # solo retorna una lista con un atributo

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
print(rel_soup.a['rel'])
# añadir un atributo más
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
print(rel_soup.a)
# se puede deshabilitar con multi_valued_attributes=None
no_list = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
print(no_list.p['class'])
