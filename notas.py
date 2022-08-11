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
find_parents(name, attrs, string, limit, **kwargs), find_parent no permite limit
"""

a_string = soup.find(string="Lacie")
print(a_string) # retorna una cadena "Lacie"
print(a_string.find_parents("a")) # retorna lo mismo pero en una lista con toda la etiqueta
print(a_string.find_parent("p")) # retorna etiqueta p y todo lo que este dentro

"""
find_previous_siblings() y find_previous_sibling()
sibling no permite limit
utilican previuos_siblings para iterar sobre los elementos
"""
last_link = soup.find("a", id="link3")
print(last_link) # etk a id link3
print(last_link.find_previous_siblings=("a"))
# retorna todas las a previos a la ultima link3
f_stroy = soup.find("p", "story")
print(f_stroy.find_previous_sibling("p")) # retorna p

# find_all_next() y find_next()

first_link = soup.a
print(first_link) # retorna a id link1
print(first_link.find_all_next(string=True))
# ['Elsie', ',\n', 'Lacie', ' and\n', 'Tillie',
#  ';\nand they lived at the bottom of a well.', '\n', '...', '\n']
print(first_link.find_next("p"))

# find_all_previous() y find_previous() itera sobre etiquetas y cadenas que van antes del documento
first_link = soup.a
print(first_link)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(first_link.find_all_previous("p"))
# [<p class="story">Once upon a time there were three little sisters; ...</p>,
#  <p class="title"><b>The Dormouse's story</b></p>]
print(first_link.find_previous("title"))
# [<p class="story">Once upon a time there were three little sisters; ...</p>,
#  <p class="title"><b>The Dormouse's story</b></p>]

"""
selectores css
bs4 tiene un select() para ejecutar un css selector contra un documento analizado y devolvera las coincidencias
"""
# encontrar las etiquetas
print(soup.select("title"))
# <title>The Dormouse's story</title>
print(soup.select("p:nth-of-type(3)"))
# [<p class="story">...</p>]
# encuenta etiquetas debajo de otras
print(soup.select("body a"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.select("html head select"))
# [<title>The Dormouse's story</title>]
# encuentra etiquetas directamente debajo de otras etiquetas
print(soup.select("head > title"))
# [<title>The Dormouse's story</title>]
print(soup.select("p"))

# encuentra etiquetas por clase
soup.select(".sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("[class~=sister]")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# busca etiquetas por ID
soup.select("#link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select("a#link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# pasar varios elementos como una tupla
soup.select("#link1,#link2")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# prueba la existencia de un atributo
soup.select('a[href]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# buscar etiquetas por valor de atributo
soup.select('a[href="http://example.com/elsie"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select('a[href^="http://example.com/"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href$="tillie"]')
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href*=".com/el"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

# primera etiqueta que coincide con un selector
soup.select_one(".sister")
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# XML define espacios de nombres
from bs4 import BeautifulSoup
xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
 <ns1:child>I'm in namespace 1</ns1:child>
 <ns2:child>I'm in namespace 2</ns2:child>
</tag> """
soup = BeautifulSoup(xml, "xml")

soup.select("child")
# [<ns1:child>I'm in namespace 1</ns1:child>, <ns2:child>I'm in namespace 2</ns2:child>]

soup.select("ns1|child")
# [<ns1:child>I'm in namespace 1</ns1:child>]

namespaces = dict(first="http://namespace1/", second="http://namespace2/")
soup.select("second|child", namespaces=namespaces)
# [<ns1:child>I'm in namespace 2</ns1:child>]

# cambiar nombres y atributos de etiquetas
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b

tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1
tag
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
tag
# <blockquote>Extremely bold</blockquote>

# modificar .string
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')

tag = soup.a
tag.string = "New link text."
tag
# <a href="http://example.com/">New link text.</a>
# cuidado al modificar etiquetas que contenga otras o seran modificadas

# append() añade contenido a una etiqueta
soup = BeautifulSoup("<a>Foo</a>", 'html.parser')
soup.a.append("Bar")

soup
# <a>FooBar</a>
soup.a.contents
# ['Foo', 'Bar']

# extend()
soup = BeautifulSoup("<a>Soup</a>", 'html.parser')
soup.a.extend(["'s", " ", "on"])

soup
# <a>Soup's on</a>
soup.a.contents
# ['Soup', ''s', ' ', 'on']

# NavigableString() y .new_tag(). agregar una cadena a un documento

soup = BeautifulSoup("<b></b>", 'html.parser')
tag = soup.b
tag.append("Hello")
new_string = NavigableString(" there")
tag.append(new_string)
tag
# <b>Hello there.</b>
tag.contents
# ['Hello', ' there']

# crear un comentario u otra subclase de NavigableString
from bs4 import Comment
new_comment = Comment("Nice to see you.")
tag.append(new_comment)
tag
# <b>Hello there<!--Nice to see you.--></b>
tag.contents
# ['Hello', ' there', 'Nice to see you.']

# crear una nueva etiqueta
soup = BeautifulSoup("<b></b>", 'html.parser')
original_tag = soup.b

new_tag = soup.new_tag("a", href="http://www.example.com")
original_tag.append(new_tag)
original_tag
# <b><a href="http://www.example.com"></a></b>

new_tag.string = "Link text."
original_tag
# <b><a href="http://www.example.com">Link text.</a></b>

# insert()
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
tag = soup.a

tag.insert(1, "but did not endorse ")
tag
# <a href="http://example.com/">I linked to but did not endorse <i>example.com</i></a>
tag.contents
# ['I linked to ', 'but did not endorse', <i>example.com</i>]

# insert_before() y insert_after()
soup = BeautifulSoup("<b>leave</b>", 'html.parser')
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_before(tag)
soup.b
# <b><i>Don't</i>leave</b>

div = soup.new_tag('div')
div.string = 'ever'
soup.b.i.insert_after(" you ", div)
soup.b
# <b><i>Don't</i> you <div>ever</div> leave</b>
soup.b.contents
# [<i>Don't</i>, ' you', <div>ever</div>, 'leave']

# clear()
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
tag = soup.a

tag.clear()
tag
# <a href="http://example.com/"></a>

# extract()
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

i_tag = soup.i.extract()

a_tag
# <a href="http://example.com/">I linked to</a>

i_tag
# <i>example.com</i>

print(i_tag.parent)
# None

my_string = i_tag.string.extract()
my_string
# 'example.com'

print(my_string.parent)
# None
i_tag
# <i></i>

# decompose() elimina una etiqueta de arbol y luego la destruye junto a su contenido
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
i_tag = soup.i

i_tag.decompose()
a_tag
# <a href="http://example.com/">I linked to</a>

# no debe usarse sino sabe lo que hace
i_tag.decomposed
# True

a_tag.decomposed
# False

# replace_with()
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

new_tag = soup.new_tag("b")
new_tag.string = "example.com"
a_tag.i.replace_with(new_tag)

a_tag
# <a href="http://example.com/">I linked to <b>example.com</b></a>

bold_tag = soup.new_tag("b")
bold_tag.string = "example"
i_tag = soup.new_tag("i")
i_tag.string = "net"
a_tag.b.replace_with(bold_tag, ".", i_tag)

a_tag
# <a href="http://example.com/">I linked to <b>example</b>.<i>net</i></a>

# warp() envuelve un elemento en la etiqueta a especificar
soup = BeautifulSoup("<p>I wish I was bold.</p>", 'html.parser')
soup.p.string.wrap(soup.new_tag("b"))
# <b>I wish I was bold.</b>

soup.p.wrap(soup.new_tag("div"))
# <div><p><b>I wish I was bold.</b></p></div>

# unwrap() elmina la etiqueta pero no su contenido
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

a_tag.i.unwrap()
a_tag
# <a href="http://example.com/">I linked to example.com</a>
# smooth
soup = BeautifulSoup("<p>A one</p>", 'html.parser')
soup.p.append(", a two")

soup.p.contents
# ['A one', ', a two']

print(soup.p.encode())
# b'<p>A one, a two</p>'

print(soup.p.prettify())
# <p>
#  A one
#  , a two
# </p>

soup.smooth()

soup.p.contents
# ['A one, a two']

print(soup.p.prettify())
# <p>
#  A one, a two
# </p>

# prettity() retorna un árbol formateado
markup = '<html><head><body><a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
soup.prettify()
# '<html>\n <head>\n </head>\n <body>\n  <a href="http://example.com/">\n...'

print(soup.prettify())
# <html>
#  <head>
#  </head>
#  <body>
#   <a href="http://example.com/">
#    I linked to
#    <i>
#     example.com
#    </i>
#   </a>
#  </body>
# </html>

# llamar a prettify() en nivel superior

# no se debe usar directamente para dar formato, solo es una manera visual de comprender la estructura

# impresion no bonita. usar str()
str(soup)
# '<html><head></head><body><a href="http://example.com/">I linked to <i>example.com</i></a></body></html>'

str(soup.a)
# '<a href="http://example.com/">I linked to <i>example.com</i></a>'

# formateadores de salida
soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.", 'html.parser')
str(soup)
# '“Dammit!” he said.'

# caracters de salida
oup = BeautifulSoup("<p>The law firm of Dewey, Cheatem, & Howe</p>", 'html.parser')
soup.p
# <p>The law firm of Dewey, Cheatem, &amp; Howe</p>

soup = BeautifulSoup('<a href="http://example.com/?foo=val1&bar=val2">A link</a>', 'html.parser')
soup.a
# <a href="http://example.com/?foo=val1&amp;bar=val2">A link</a>

french = "<p>Il a dit &lt;&lt;Sacr&eacute; bleu!&gt;&gt;</p>"
soup = BeautifulSoup(french, 'html.parser')
print(soup.prettify(formatter="minimal"))
# <p>
#  Il a dit &lt;&lt;Sacré bleu!&gt;&gt;
# </p>

# convierte caracteres unicode a entidades HTML, si es posible
print(soup.prettify(formatter="html"))
# <p>
#  Il a dit &lt;&lt;Sacr&eacute; bleu!&gt;&gt;
# </p>

br = BeautifulSoup("<br>", 'html.parser').br

print(br.encode(formatter="html"))
# b'<br/>'

print(br.encode(formatter="html5"))
# b'<br>'

option = BeautifulSoup('<option selected=""></option>').option
print(option.encode(formatter="html"))
# b'<option selected=""></option>'

print(option.encode(formatter="html5"))
# b'<option selected></option>'

# usar un control mas sofisticado
from bs4.formatter import HTMLFormatter
def uppercase(str):
    return str.upper()

formatter = HTMLFormatter(uppercase)

print(soup.prettify(formatter=formatter))
# <p>
#  IL A DIT <<SACRÉ BLEU!>>
# </p>

print(link_soup.a.prettify(formatter=formatter))
# <a href="HTTP://EXAMPLE.COM/?FOO=VAL1&BAR=VAL2">
#  A LINK
# </a>

# formateo que aumenta la sangria
formatter = HTMLFormatter(indent=8)
print(link_soup.a.prettify(formatter=formatter))
# <a href="http://example.com/?foo=val1&bar=val2">
#         A link
# </a>

# subclasificacion sobre la salida para dar más control
attr_soup = BeautifulSoup(b'<p z="1" m="2" a="3"></p>', 'html.parser')
print(attr_soup.p.encode())
# <p a="3" m="2" z="1"></p>

# para desactivas usar el metodo Formatter.attributes() para controlar que atributos se omiten y en que orden
class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            if k == 'm':
                continue
            yield k, v

print(attr_soup.p.encode(formatter=UnsortedAttributes()))
# <p z="1" a="3"></p>

from bs4.element import CData
soup = BeautifulSoup("<a></a>", 'html.parser')
soup.a.string = CData("one < three")
print(soup.a.prettify(formatter="html"))
# <a>
#  <![CDATA[one < three]]>
# </a>

# get_text() formato legible para humanos dentro de un documento o etiqueta
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, 'html.parser')

soup.get_text()
'\nI linked to example.com\n'
soup.i.get_text()
'example.com'

# usar .stripped_strings
[text for text in soup.stripped_strings]
# retorna una lista de items

# diferencias entre analizadores
BeautifulSoup("<a><b/></a>", "html.parser")
# <a><b></b></a>

print(BeautifulSoup("<a><b/></a>", "xml"))
# <?xml version="1.0" encoding="utf-8"?>
# <a><b/></a>

# ver diferencias
BeautifulSoup("<a></p>", "lxml")
# <html><body><a></a></body></html>
# contra el mismo usando html5lib
BeautifulSoup("<a></p>", "html5lib")
# <html><head></head><body><a><p></p></a></body></html>
# el mismo incorporando el analizador de python
BeautifulSoup("<a></p>", "html.parser")
# <a></a>

# encodings
markup = "<h1>Sacr\xc3\xa9 bleu!</h1>"
soup = BeautifulSoup(markup, 'html.parser')
soup.h1
# <h1>Sacré bleu!</h1>
soup.h1.string
# 'Sacr\xe9 bleu!'

soup.original_encoding
'utf-8'

markup = b"<h1>\xed\xe5\xec\xf9</h1>"
soup = BeautifulSoup(markup, 'html.parser')
print(soup.h1)
# <h1>νεμω</h1>
print(soup.original_encoding)
# iso-8859-7
# se arregla así
soup = BeautifulSoup(markup, 'html.parser', from_encoding="iso-8859-8")
print(soup.h1)
# <h1>םולש</h1>
print(soup.original_encoding)
# iso8859-8

# usar exclude_encoding si no se sabe la codificacion correcta
soup = BeautifulSoup(markup, 'html.parser', exclude_encodings=["iso-8859-7"])
print(soup.h1)
# <h1>םולש</h1>
print(soup.original_encoding)
# WINDOWS-1255

# codificacion de salida. automaticamente al crea un documento se crea en UTF-8 aunque no se especifique
markup = b'''
 <html>
  <head>
   <meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type" />
  </head>
  <body>
   <p>Sacr\xe9 bleu!</p>
  </body>
 </html>
'''

soup = BeautifulSoup(markup, 'html.parser')
print(soup.prettify())
# <html>
#  <head>
#   <meta content="text/html; charset=utf-8" http-equiv="Content-type" />
#  </head>
#  <body>
#   <p>
#    Sacré bleu!
#   </p>
#  </body>
# </html>

# user prettify si no desea utf-8
print(soup.prettify("latin-1"))
# <html>
#  <head>
#   <meta content="text/html; charset=latin-1" http-equiv="Content-type" />
# ...

from bs4 import UnicodeDammit
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit.unicode_markup)
# Sacré bleu!
dammit.original_encoding
# 'utf-8'

# comillas tipograficas
markup = b"<p>I just \x93love\x94 Microsoft Word\x92s smart quotes</p>"

UnicodeDammit(markup, ["windows-1252"], smart_quotes_to="html").unicode_markup
# '<p>I just &ldquo;love&rdquo; Microsoft Word&rsquo;s smart quotes</p>'

UnicodeDammit(markup, ["windows-1252"], smart_quotes_to="xml").unicode_markup
# '<p>I just &#x201C;love&#x201D; Microsoft Word&#x2019;s smart quotes</p>'

# comillas tipograficas de microsoft en ascii
UnicodeDammit(markup, ["windows-1252"], smart_quotes_to="ascii").unicode_markup
# '<p>I just "love" Microsoft Word\'s smart quotes</p>'

UnicodeDammit(markup, ["windows-1252"]).unicode_markup
# '<p>I just “love” Microsoft Word’s smart quotes</p>'

# condiciones inconsistentes
snowmen = (u"\N{SNOWMAN}" * 3)
quote = (u"\N{LEFT DOUBLE QUOTATION MARK}I like snowmen!\N{RIGHT DOUBLE QUOTATION MARK}")
doc = snowmen.encode("utf8") + quote.encode("windows_1252")

# numero de lineas puede encontrar la posicion de donde encontro la etiqueta
markup = "<p\n>Paragraph 1</p>\n    <p>Paragraph 2</p>"
soup = BeautifulSoup(markup, 'html.parser')
for tag in soup.find_all('p'):
    print(repr((tag.sourceline, tag.sourcepos, tag.string)))
# (1, 0, 'Paragraph 1')
# (3, 4, 'Paragraph 2')

soup = BeautifulSoup(markup, 'html5lib')
for tag in soup.find_all('p'):
    print(repr((tag.sourceline, tag.sourcepos, tag.string)))
# (2, 0, 'Paragraph 1')
# (3, 6, 'Paragraph 2')

# descativar la funcion
markup = "<p\n>Paragraph 1</p>\n    <p>Paragraph 2</p>"
soup = BeautifulSoup(markup, 'html.parser', store_line_numbers=False)
print(soup.p.sourceline)
# None

# corey bs4
from bs4 import BeautifulSoup
import requests

with open('sample.html', 'rb') as f:
    soup = BeautifulSoup(f, 'html.parser')

print(soup.find('div', class_='article'))
# busca un div que contenga article

# usar la funcion .find dentro de un bucle

for article in soup.find_all('div', class_='article'):
    head = article.h2.a.text
    print(head)

    summary = article-p.text
    print(summary)

# usar una url real en bs4
from bs4 import BeautifulSoup
import requests

url = 'http://coreyms.com'
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')

article = soup.find('article')

head = article.h2.a.text
summary = article.find('div', class_='entry-content').p.text
# acceder al video
vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)
# separar la url de video y cambiar por wathc?v={url}
vid_id = vid_src.split('/')[4] # separa por /
vid_id = vid_id.split('?')[0] # obtiene el id
print(vid_id)
# usar url youtube + wathc?v=id
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(ty_link)

# usar un bucle para obtener todo
from bs4 import BeautifulSoup
import requests

url = 'http://coreyms.com'
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')

for article in soup.find_all('div'):
    head = article.h2.a.text
    print(head)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    yt_link = f"https://youtube.com/watch?v={vid_id}"
    print(yt_link)
    print()
# funciona pero aparece un error con los videos lo cual se soluciona manejando las excepciones
try:
    vid_src = article.find('iframe', class_='entry-contet')['src']
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    yt_link = f"https://youtube.com/watch?v={vid_id}"
except Exception as e:
    yt_link = None
print(yt_link)
print()
# guardar los resultado en .csv
from bs4 import BeautifulSoup
import requests
import csv

url = 'https://coreyms.com'
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')

with open('corey.csv', 'w', newline='') as f:
    head_title = ['title', 'desc', 'youtube-link']
    esc = csv.writer(f)
    esc.writerow(head_link)

    for article in soup.find_all('article'):
        head = article.h2.a.text
        print(head)
        summary = article.find('div', class_='entry-content').p.text
        print(summary)

        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            yt_link = f"https://youtube.com/watch?v={vid_id}"
        except Exception as e:
            yt_link = None
        print(yt_link)
        print()
        esc.writerow([head, summary, yt_link])
