import sqlite3
import unicodedata
import re

DB_NAME = "processador_frases.db"

def remover_acentos(texto):
    """Remove acentos do texto"""
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def limpar_texto(texto):
    """Remove pontuações e converte para minúsculas"""
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    return texto

def tokenizar(texto):
    """Divide o texto em palavras (tokenização simples)"""
    return texto.split()

def remover_stopwords(tokens):
    """Remove stopwords da lista de tokens"""
    stopwords = {"o", "a", "os", "as", "de", "do", "da", "um", "uma", "é", "e", "com", "para"}  # Lista manual
    return [palavra for palavra in tokens if palavra not in stopwords]

def processar_texto(texto):
    """Executa todo o pré-processamento: normalização, tokenização e remoção de stopwords"""
    texto = remover_acentos(texto)
    texto = limpar_texto(texto)
    tokens = tokenizar(texto)
    tokens_sem_stopwords = remover_stopwords(tokens)
    return tokens_sem_stopwords

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

if __name__ == "__main__":
    frase = "O cachorro corre rápido pelo parque."
    tokens_processados = processar_texto(frase)
    analise = analisar_sintaxe(tokens_processados)

    print("Tokens processados:", tokens_processados)
    print("Análise Sintática:", analise)