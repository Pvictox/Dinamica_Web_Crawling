import xml.dom.minidom
from Modelos.Pagina import Pagina
import ControlPagina
import operator

DOMTREE = xml.dom.minidom.parse("verbetesWikipedia.xml")
collection = DOMTREE.documentElement


cont = 0

dicionarioPaginas = dict()
dicionarioPaginas = Pagina.buildModelXML(collection=collection, dicionarioPaginas=dicionarioPaginas)


palavra = "computer"
ControlPagina.aplicarRelevancia(palavra, dicionarioPag=dicionarioPaginas)

listaRelevante = []
for key, value in dicionarioPaginas.items():
    if (value.getRelevancia() > 0):
        listaRelevante.append(value)

listaRelevante.sort(key=lambda x:x.getRelevancia(), reverse=True)
print(len(listaRelevante))

for pg in listaRelevante:
    if (cont < 5):
        print(pg.toString())
        cont+=1


