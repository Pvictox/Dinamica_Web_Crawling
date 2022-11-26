def aplicarRelevancia(termo, dicionarioPag):
    split_Termo = termo.split(" ")
    if (len(split_Termo) == 1): # 1 palavra só
        for key,value in dicionarioPag.items():
            value.addRelevancia(calcularRelevancia(termo=split_Termo[0], pagina=value))
    elif (len(split_Termo) == 2):
        for key,value in dicionarioPag.items():
            relevanciaTermo1 = 0
            relevanciaTermo2 = 0
            relevanciaTermo1 = calcularRelevancia(termo=split_Termo[0], pagina=value)
            relevanciaTermo2 = calcularRelevancia(termo=split_Termo[1], pagina=value)
            print("REL termo 1: ", relevanciaTermo1)
            print("REL termo 2: ", relevanciaTermo2)


def calcularRelevancia(termo, pagina):
    relevanciaTermo = 0        
    if (pagina.getTitulo().lower().__contains__(termo)): #Verifica titulo
        relevanciaTermo+=10
    if (pagina.getTexto().lower().__contains__(termo)):
        texto_Split = pagina.getTexto().lower().split(" ")
        relevanciaTermo += texto_Split.count(termo)
    return relevanciaTermo
