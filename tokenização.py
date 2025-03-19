def remover_acentos(texto):
    mapa_acentos = {
        "á": "a", "à": "a", "ã": "a", "â": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "õ": "o", "ô": "o",
        "ú": "u",
        "ç": "c"
    }

    return "".join(mapa_acentos.get(char, char) for char in texto)


def lematizar(palavra):
    lemas = {
        "bons": "bom", "felizes": "feliz", "otimos": "otimo",
        "ruins": "ruim", "tristes": "triste", "pessimos": "pessimo",
        "horriveis": "horrivel", "maravilhosos": "maravilhoso"
    }

    sufixos = ["ndo", "ando", "endo", "mente", "veis", "veis", "s"]
    palavra = palavra.lower()

    if palavra in lemas:
        return lemas[palavra]

    for sufixo in sufixos:
        if palavra.endswith(sufixo):
            return palavra[:-len(sufixo)]

    return palavra
