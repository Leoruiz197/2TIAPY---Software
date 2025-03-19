import sqlite3

DB_NAME = "processador_frases.db"

def buscar_tipo_palavra(palavra):
    """Busca o tipo da palavra no banco de dados"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT tipo FROM palavras WHERE palavra = ?", (palavra.lower(),))
    resultado = cursor.fetchone()

    conn.close()
    return resultado[0] if resultado else "outro"

def analisar_sintaxe(tokens):
    """Classifica palavras dinamicamente com base no banco de dados"""
    estrutura = {
        "sujeito": [],
        "verbo": [],
        "complemento": [],
        "outros": []
    }

    for palavra in tokens:
        tipo = buscar_tipo_palavra(palavra)

        if tipo == "substantivo":
            estrutura["sujeito"].append(palavra)
        elif tipo == "verbo":
            estrutura["verbo"].append(palavra)
        elif tipo == "adjetivo":
            estrutura["complemento"].append(palavra)
        else:
            estrutura["outros"].append(palavra)

    return estrutura