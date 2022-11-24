def aplicarRelevancia(termo, dicionarioPag):
    split_Termo = termo.split(" ")
    if (len(split_Termo) == 1): # 1 palavra só
        for key,value in dicionarioPag.items():
            value.setRelevancia(0)
            if (value.getTitulo().lower().__contains__(split_Termo[0])): #Verifica titulo
                value.addRelevancia(10)
            if (value.getTexto().lower().__contains__(split_Termo[0])):
                texto_Split = value.getTexto().lower().split(" ")
                value.addRelevancia(texto_Split.count(split_Termo[0]))  
        