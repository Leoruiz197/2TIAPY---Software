import sqlite3

DB_NAME = "processador_frases.db"

def criar_banco():
    """Cria as tabelas do banco de dados para palavras-chave"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palavras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palavra TEXT NOT NULL UNIQUE,
            tipo TEXT CHECK(tipo IN ('substantivo', 'verbo', 'adjetivo'))
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco()