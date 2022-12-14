
cache = dict()

def searchTermo(termo, dicionarioPag):
    result = dict()
    termo_splitado = termo.lower().split(" ")
    if (len(cache) > 19):
        cache.clear()
    if (len(termo_splitado) == 1):
        if (termo_splitado[0] in cache):
            print("Palavra previamente pesquisada | Retornando Cache")
            return cache[termo_splitado[0]]
        else:    
            for key,value in dicionarioPag.items():
                dicionarioTitulo = value.getPalavrasTitulo()
                relevanciaTermoTitulo = 0
                if (termo_splitado[0] in dicionarioTitulo):
                    relevanciaTermoTitulo = dicionarioTitulo[termo_splitado[0]] * 30  
                relevanciaTermoTexto = 0
                if (termo_splitado[0] in value.getPalavrasTexto()):
                    relevanciaTermoTexto = value.getPalavrasTexto()[termo_splitado[0]] * 10
                result[value] = relevanciaTermoTexto+relevanciaTermoTitulo
            cache[termo_splitado[0]] = result
            return result
    elif(len(termo_splitado) == 2):
        termo = termo.lower()
        if (termo in cache):
            print("Palavra previamente pesquisada | Retornando Cache")
            return cache[termo]
        else:
            for key, value in dicionarioPag.items():
                dicionarioTitulo = value.getPalavrasTitulo()
                termo1 = termo_splitado[0]
                termo2 = termo_splitado[1]
                relevanciaTermo1 = 0
                relevanciaTermo2 = 0
                if (termo1 in dicionarioTitulo):
                    relevanciaTermo1 = dicionarioTitulo[termo1] * 30
                if (termo2 in dicionarioTitulo):
                    relevanciaTermo2 = dicionarioTitulo[termo2] * 30
                if (termo1 in value.getPalavrasTexto()):
                    relevanciaTermo1 = value.getPalavrasTexto()[termo1] * 10
                if (termo2 in value.getPalavrasTexto()):
                    relevanciaTermo2 = value.getPalavrasTexto()[termo2] * 10
                
                pesoTermo1 = 50
                pesoTermo2 = 50
                relevanciaPonderada = 0
                if (relevanciaTermo1 != 0 and relevanciaTermo2 != 0):
                    pesoTermo1 = pesoTermo1- (0.1*relevanciaTermo1)
                    relevanciaTermo1 = (relevanciaTermo1*pesoTermo1)//100
                    pesoTermo2 = pesoTermo2- (0.1*relevanciaTermo2)
                    relevanciaTermo2 = (relevanciaTermo2*pesoTermo2)//100
                    relevanciaPonderada = relevanciaTermo2+relevanciaTermo1
                result[value] = relevanciaPonderada
            cache[termo] = result
            return result

        

                 



def termosEmPagina(dicionarioPag):
    for key, value in dicionarioPag.items():
        palavras_titulo_pagina = value.getTitulo().lower().split(" ")
        dictTitulo = applyRelevanciaCadaPalavra(palavras_titulo_pagina)
        value.setPalavrasTitulo(dictTitulo)
        palavras_texto_pagina = value.getTexto().lower().split(" ")
        dictTexto = applyRelevanciaCadaPalavra(palavras_texto_pagina)
        value.setPalavrasTexto(dictTexto)



def applyRelevanciaCadaPalavra(conjPalavras):
    dicionarioRelevancia = dict()
    for palavra in conjPalavras:
        if (len(palavra) > 3):
            if (palavra in dicionarioRelevancia):
                dicionarioRelevancia[palavra] += int(1)
            else:
                dicionarioRelevancia[palavra] = int(1)
    return dicionarioRelevancia    
            


