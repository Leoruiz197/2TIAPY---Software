def identificador_de_sujeito(frase):
    palavras = frase.split()

    pronomes = ["eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas"]
    artigos  = ["o", "a", "os", "as", "um", "uma", "uns", "umas"]
    sujeito  = ""

    for item, palavra in enumerate(palavras):
        if palavra.lower() in artigos: # Regras 1 - Artigos
            if item < len(palavras)-1:
                print("Regra 1")
                print(sujeito)
                sujeito = palavras[item+1]

        elif palavra.lower() in pronomes: # Regra 2 - Lista de pronomes
            print("Regra 2")
            print(sujeito)
            sujeito = palavra

        if palavra != palavras[0]:
            if palavra[0] == palavra[0].upper(): # Regra 3 - Identificar nomes próprios
                print("Regra 3")
                print(sujeito)
                sujeito = palavra

        if sujeito != "":
            break
    
    if sujeito:
        return f"O sujeito da frase '{frase}' é '{sujeito}'"

    else:
        return f"A frase não tem sujeito ou ele está oculto"

print(identificador_de_sujeito("Vamos de férias."))