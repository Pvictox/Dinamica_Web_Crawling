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
            
            #Ponderada
            pesoTermo1 = 50
            pesoTermo2 = 50
            if (relevanciaTermo1 != 0 and relevanciaTermo2 != 0):
                pesoTermo1 = pesoTermo1- (0.1*relevanciaTermo1)
                relevanciaTermo1 = (relevanciaTermo1*pesoTermo1)//100
                pesoTermo2 = pesoTermo2- (0.1*relevanciaTermo2)
                relevanciaTermo2 = (relevanciaTermo2*pesoTermo2)//100
                relevanciaPonderada = relevanciaTermo2+relevanciaTermo1
            else:
                relevanciaPonderada = 0
            

            #Busca pela junção completa
            relevanciaTermoJuncao = calcularRelevanciaTermoJunto(termo=termo, pagina=value)
        
            value.setRelevancia((relevanciaPonderada+relevanciaTermoJuncao)/2)


                 


def calcularRelevanciaTermoJunto(termo, pagina):
    relevanciaTermo = 0        
    if (pagina.getTitulo().lower().__contains__(termo)): #Verifica titulo
        relevanciaTermo+=40
    if (pagina.getTexto().lower().__contains__(termo)):
        relevanciaTermo += pagina.getTexto().lower().count(termo)*20
    return relevanciaTermo

def calcularRelevancia(termo, pagina):
    relevanciaTermo = 0        
    if (pagina.getTitulo().lower().__contains__(termo)): #Verifica titulo
        relevanciaTermo+=10
    if (pagina.getTexto().lower().__contains__(termo)):
        texto_Split = pagina.getTexto().lower().split(" ")
        relevanciaTermo += texto_Split.count(termo)
    return relevanciaTermo
