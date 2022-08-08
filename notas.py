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
una etiqueta puede tener cualquier numero de atributos. la etiqueta <b id='boldest'> tiene un atributo id con valor 'boldest'.
se puede acceder a los atributos tratando las etiquetas como un diccionario"""
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
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
print(no_list.p['class']) # retorna una cadena
# se puede usar get_attribute_list para obtener simpe una lista, sea o no un multiatribut
print(no_list.p.get_attribute_list)
print(no_list.p.get_attribute_list('class'))
# sin analiza un documento con XML, no hay atributos de varios valores
xml_soup = BeautifulSoup('<p class="body strikeout"></p>','xml')
print(xml_soup.p['class'])
# puede que no sea necesario hacer esto, pero de ser así se debe seguir la reglas especificas
from b4s.builder import builder_registry
builder_registry.lookup('html').DEFAULT_CDATA_LIST_ATTRIBUTES

"""
NavigableString
una cadena corresponde a un fragmento de texto dentro de una etiqueta
obtiene el texto de la etiqueta no los atributos
"""
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(tag.string)
print(type(tag.string))
"""
NavigableString es como una cadena unicode de python, excepto que tambien es compatible
con navegción de árbol y busqueda de árbol
usar str para convertir a string
"""
tag_string = str(tag.string)
print(tag_string, type(tag_string))
# no se puede editar pero se puede reemplazar con replace_with()
tag.strin.replace_with("no longer bold")
print(tag)

"""
BeautifulSoup
representa el documento analizado como un entero. para la mayoria de los propositos,
puede tratarlo como una etiqueta de objeto. Esto significa que es compatible con
la mayoria de los metodos descritos: navegacion y busqueda por arbol.

Tambien puede pasar un BeautifulSoup como objeto a para modificar un árbol como
lo haría con los etiquetas.
"""
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
print(doc)
# el atributo no corresponde a una etiqueta real HTML o XML, pero a veces es util para usar value.name
print(doc.name)

"""
Comentario y otras cadenas especiales
el principal problema a encontrar es el comentario
"""
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(comment, type(comment))
# el objeto comment es solo un tipo especial de NavigableString
print(comment.string)
# pero cuando aparece como parte de un doc HTML, un comment se muestra con un formato especial
print(soup.b.prettify())
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
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
"""
Bajando
las etiquetas pueden contener cadenas y otras etiquetas.
chilrens
BeautifulSoup no son compatibles con ninguno de estos atributos, porque una
cadena no puede contener atributos.
"""
# navegación usando nombre de etiqueta
# la forma más sencilla es por el nombre (tipo) de etiqueta
print(soup.head) # accede al encabezado
print(soup.title) # accede al titulo
# repeter este truco hasta acercarte a una determinada parte del árbol dentro del body
print(soup.body.p)
# el uso de un nombre de etiqueta solo retorna la primera etiqueta del doc
print(soup.a)
# si se desea por ejemplo todas las etiquetas <a>
soup.find_all('a')
# .contents y .childrens
# los hijos de una etiqueta están disponibles en una lista llamada .contents
head_tag = soup.head
print(head_tag)
print(head_tag.contents)
title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)
# la etiqueta <html> es hija de BeautifulSoup
print(len(soup.contents))
print(soup.contents[1].name)
# una cadena no tiene .contents porque no puede contener cualquier cosa
text = title.contents[0]
print(text.contents) # retorna error
# se puede itera sobre una etiqueta children usando un generador .children
for child in title_tag.chilren:
    print(child)
# .descendants permite iterar sobre todos los hijos de una etiqueta
for child in head_tag.descendants:
    print(child)
# la etiqueta head solo tiene un hijo, pero tiene dos descendientes: title y el hijo de title
print(len(list(soup.children)))
print(len(list(soup.descendants)))

# .string si una etiqueta tiene un solo hijo y es un NavigableString, entonces está disponible como .string
print(title_tag.string)
# si el unico hijo de un etiqueta es una etiqueta y esa tiene un string, entonces la principal es .string
print(head_tag.contents)
print(head_tag.string)
# si la etiqueta contiene más de una cosa, entonces no se puede usar .string o retorna None
print(soup.html.string)
"""
.string y stripped_strings
si hay más de una cosa dentro de un etiqueta, utilizar .strings
"""
for string in soup.strings:
    print(repr(string)) # repr retornas los valores de escape


