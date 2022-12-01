from collections import defaultdict

class Pagina:
    def __init__(self, id, titulo, texto):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.links = []
        self.relevancia = 0
        self.palavrasTitulo = dict()
        self.palavrasTexto = dict()
    

    def getPalavrasTitulo(self):
        return self.palavrasTitulo

    def getPalavrasTexto(self):
        return self.palavrasTexto

    def setPalavrasTitulo(self,valor):
        self.palavrasTitulo = valor

    def setPalavrasTexto(self,valor):
        self.palavrasTexto = valor

    def addLink(self, idLink):
        self.links.append(idLink)
    
    def addRelevancia(self, valor):
        self.relevancia +=valor
    
    def getRelevancia(self):
        return self.relevancia
    
    def setRelevancia(self, valor):
        self.relevancia = valor

    def getTexto(self):
        return self.texto

    def getID(self):
        return self.id

    def getTitulo(self):
        return self.titulo

    def toString(self):
        return "Id: "+str(self.id)+" | Titulo: "+str(self.titulo)+" | Relevancia: "+str(self.relevancia)

    def setTitulo(self, valor):
        self.titulo = valor
    
    def setTexto(self, valor):
        self.texto = valor
    
    def buildModelXML(collection, dicionarioPaginas):
        pages = collection.getElementsByTagName("page")
        cont = 0
        for pagina in pages:
            id_sala =  pagina.getElementsByTagName("id")[0].childNodes[0].nodeValue
            title = pagina.getElementsByTagName("title")[0].childNodes[0].nodeValue
            textoSala = pagina.getElementsByTagName("text")[0].childNodes[0].nodeValue
            pagAtual = Pagina(id=id_sala, titulo=title, texto=textoSala)
            dicionarioPaginas[cont] = pagAtual
            cont+=1
        return dicionarioPaginas