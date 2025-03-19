import sqlite3

DB_NAME = "processador_frases.db"

def criar_banco():
    """Cria o banco de dados se ele não existir."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS frases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto_original TEXT NOT NULL,
            texto_processado TEXT,
            tokenizacao TEXT,
            analise_sintatica TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS regras_gramaticais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            regra TEXT NOT NULL,
            descricao TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Chamando a criação do banco de dados automaticamente ao importar o módulo
criar_banco()

def inserir_frase(texto_original, texto_processado, tokenizacao, analise_sintatica):
    """Insere uma nova frase no banco de dados"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO frases (texto_original, texto_processado, tokenizacao, analise_sintatica) 
        VALUES (?, ?, ?, ?)
    ''', (texto_original, texto_processado, tokenizacao, analise_sintatica))

    conn.commit()
    conn.close()
    print("Frase inserida com sucesso!")

def recuperar_frases():
    """Recupera todas as frases armazenadas"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM frases ORDER BY data_criacao DESC")
    frases = cursor.fetchall()

    conn.close()
    return frases