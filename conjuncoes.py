# Função simples para encontrar as conjunções
def encontrar_conjuncoes(texto: str) -> list:
    """
       Identifica e retorna as conjunções presentes em um texto.

       A função verifica cada palavra do texto para determinar se é uma conjunção.
       Utiliza uma lista abrangente de conjunções da língua portuguesa, incluindo
       conjunções coordenativas e subordinativas.

       Parâmetros:
       -----------
       texto : str
           O texto a ser analisado.

       Retorna:
       --------
       list
           Uma lista contendo as conjunções encontradas no texto.

       Exemplo de uso:
       ---------------
       >>> encontrar_conjuncoes("Quero sair, mas está chovendo e não trouxe guarda-chuva.")
       ['mas', 'e']
   """

    # Lista de conjunções comuns em português
    conjuncoes = {
        # Conjunções Coordenativas
        "e", "nem", "mas", "porém", "contudo", "todavia", "entretanto", "senão",
        "logo", "portanto", "assim", "por conseguinte", "pois", "porque", "porquanto",
        "ou", "ora", "já", "quer", "seja", "não só", "mas também", "não apenas", "como também",

        # Conjunções Subordinativas
        "que", "porque", "porquanto", "pois", "como", "visto que", "já que", "uma vez que",
        "se", "caso", "contanto que", "desde que", "a menos que", "salvo se",
        "embora", "ainda que", "mesmo que", "se bem que", "posto que", "por mais que",
        "conquanto", "quando", "enquanto", "assim que", "logo que", "antes que", "depois que",
        "desde que", "tão logo", "tanto que", "de modo que", "de forma que", "de maneira que",
        "de sorte que", "como", "conforme", "segundo", "consoante", "para que", "a fim de que"
    }

    # Tokenização simples
    palavras = texto.lower().split()

    # Filtrar as palavras que são conjunções
    conjuncoes_encontradas = [ palavra for palavra in palavras if palavra in conjuncoes ]

    return conjuncoes_encontradas



#if __name__ == '__main__':
#    texto_exemplo = "Estou cansada porém preciso trabalhar."
#    print(encontrar_conjuncoes(texto_exemplo))
