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

# la cadena contiene muchos espacios en blanco, se pueden eliminar usando .stripped_strings
for string in soup.stripped_strings:
    print(repr(string))
# elimina las líneas, espacio al inicio y fin que esten en blanco
# subiendo cada cadena y etiquetan tiene un padre
"""
.parent
en el doc la etiqueta <head> es el padre de <title>
"""
title_tag = soup.title
print(title_tag)
print(title_tag.parent)
print(title_tag.string.parent)
# el padre de una etiqueta
html_tag = soup.html
print(type(html_tag))
# y el .parent de un objeto se define como None
print(soup.parent)
# .parents puede iterar sobre todos los padre de un elemento
link = soup.a
print(link)
for parent in link.parents:
    print(link.name)

# yendo de lado. usando un doc simple
si_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
print(si_soup.prettify())
# b y c hastan al mismo nivel, lo que las hace hermanos
"""
.next_sibling y .previuos_sibling
se pueden usar para navegar entre elementos de pagina que están al mismo nivel
"""
print(sibling_soup.b.next_sibling)
print(sibling_soup.b.previuos_sibling)

link = soup.a
print(link)
print(link.next_sibling)
print(link.next_sibling.next_sibling)

for si in soup.a.next_siblings:
    print(repr(si))

for si in soup.find(id='link3').previuos_siblings:
    print(repr(si))

# buscando en el árbol find() y find_all() son los más importantes
doc_soup = BeautifulSoup(html_doc, 'html.parser')

# pasar una cadena como argumento para que b4s lo busque
soup.find_all('b')
# expreciones regulares. buscar todas las etiquetas que inicien con b
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# el siguiente trae todo lo que contenga una 't'
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
# pasar una lista como argumento

print(soup.find_all(["a", "b"]))

# true. coincide con todo lo que encuentro pero no las cadenas
for tag in soup.find_all(True):
    print(tag.name)

# funciones
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_not_id)
# la funcion anterior solo retorna etiquetas <p>
# funcion que ignore cierto valor dentro de un href

def not_lacie(href):
    return href and not re.compile("lacie").search(href)

print(soup.find_all(href=not_lacie))
# la siguiente funcione retorna True si la etiqueta esta rodeada por texto
from bs4 import NavigableString

def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)

# find_all(): metodos find_all(name, attr, recursive, string, limit, **kwargs)
# busca y recupera todos los descendientes que coincidan con el filtro
soup.find_all("title")
print(soup.find_all("a", "title"))
print(soup.find_all("a"))
print(soup.find_all(id="link2"))
print(soup.find(string=re.compile("sisters")))

# argumentos de palabra. bs4 filtrara segun el atributo 'id'
print(soup.find_all(id="link2"))
# bs4 filtrara contra el href de cada etiqueta
print(soup.find_all(href=re.compile("elsie")))
# encontrar todas las etiquetas con 'id' sin importar su valor
print(find_all(id=True))
# filtrar por varios atributos
print(find_all(href=re.compile("elsie"), id="link1"))
# algunos atributos de HTML5 no se puede usar
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
print(data_soup.find_all(data-foo="value")) # error syntax
# para realizar la busqueda se puede pasar como un dict
print(data_soup.find_all(attrs={"data-fo":"value"}))
# buscando por class en css. se debe usar class_
print(soup.find_all("a", class_"sisters"))

# funcion de largo en class_, retorna todas las etiquetas que tengan una clases, que no esten vacias y su largo sea 6
print(soup.find_all(class_=re.compile("itl")))

def six_class(css_class):
    return css_class is not None and len(css_class) == 6

print(soup.find_all(class_=six_class))

# argumentos string busca cadenas en lugar de etiquetas
print(soup.find(strinf="Eslie"))
# pasarle una lista
print(soup.find_all(string=["Elsie", "Lacie"]))
print(soup.find_all(string=re.compile("Dormouse")))

def string_tag(s):
    return (s == s.parent.strin)

print(soup.find_all(string=string_tag))
# retorna
# ["The Dormouse's story", "The Dormouse's story", 'Elsie', 'Lacie', 'Tillie', '...']

# encontrar etiqueta 'a' que contenga 'Elsie'
print(soup.find_all("a", "Elsie"))

"""
el argumento limit
devuelve todas las etiquetas y cadenas que concidan con el filtro. puede tomar tiempo con doc grandes
utiliza la palabra limit para limitar el maximo de retorno
"""
print(soup.find_all("a", limit=2))
# retorna solo 2 'a' del maximo 3

"""
argumento recursive
por defecto examina todos los hijos, para traer solo los child directo usar recursive=False
"""
print(soup.html.find_all("title"))
# retorna etiqueta title
print(soup.find_all("title", recursive=False))
# retorna una lista vacia

"""
llamar una etiqueta es como llamar a find_all().
las siguiente dos lineas son equivalentes
"""
print(soup.find_all("a"))
print(soup("a"))
# las siguientes tambien son equivalentes
print(soup.title.find_all(string=True))
print(soup.title(string=True))
# find()
print(soup.find_all("title", limit=1))
# retorna una lista de solo un elemento de title
print(soup.find("title"))
# retorna lo mismo en cadena, al usar el nombre de etiqueta solo accede al primer elemento con esa etiqueta

"""
find_parents() y find_parent()
find_parent(name, attrs, string, limit, **kwargs), find_parents no permite limit
"""

a_string = soup.find(string="Lacie")
print(a_string) # retorna una cadena "Lacie"
print(a_string.find_parents("a")) # retorna lo mismo pero en una lista con toda la etiqueta
print(a_string.find_parent("p")) # retorna etiqueta p y todo lo que este dentro

