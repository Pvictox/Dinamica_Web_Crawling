import xml.dom.minidom
from Modelos.Pagina import Pagina
import ControlPagina
import operator

DOMTREE = xml.dom.minidom.parse("verbetesWikipedia.xml")
collection = DOMTREE.documentElement


cont = 0

dicionarioPaginas = dict()
dicionarioPaginas = Pagina.buildModelXML(collection=collection, dicionarioPaginas=dicionarioPaginas)



palavra = "computer science"

ControlPagina.termosEmPagina(dicionarioPag=dicionarioPaginas)

cont = 0

while (cont < 2):
    termo = input("Digite o termo\n")
    contAmostra = 0
    resultado = ControlPagina.searchTermo(termo=termo, dicionarioPag=dicionarioPaginas)
    listaRelevante = []
    resultado = sorted(resultado.items(), key=lambda x : x[1], reverse=True)
    print("============== RESULTADOS ================= ")
    for x in resultado:
        if (x[1] > 0):
            if (contAmostra < 30):
                print("Titulo: "+x[0].getTitulo() + "| Relevancia: "+str(x[1]))
                contAmostra+=1
    print("============== RESULTADOS ================= ")
# ======== BUSCA POR UMA PALAVRA ============
# ControlPagina.aplicarRelevancia(palavra, dicionarioPag=dicionarioPaginas)

# listaRelevante = []
# for key, value in dicionarioPaginas.items():
#     if (value.getRelevancia() > 0):
#         listaRelevante.append(value)

# listaRelevante.sort(key=lambda x:x.getRelevancia(), reverse=True)
# #print(len(listaRelevante))

# for pg in listaRelevante:
#     if (cont < 5):
#         print(pg.toString())
#         cont+=1
    
# ==========================================


