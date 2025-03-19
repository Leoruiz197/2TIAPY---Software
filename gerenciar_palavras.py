import sqlite3

DB_NAME = "processador_frases.db"

def inserir_palavra(palavra, tipo):
    """Adiciona uma palavra ao banco de dados"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO palavras (palavra, tipo) VALUES (?, ?)", (palavra.lower(), tipo))
        conn.commit()
        print(f"Palavra '{palavra}' adicionada como '{tipo}'.")
    except sqlite3.IntegrityError:
        print(f"A palavra '{palavra}' já existe no banco.")

    conn.close()

if __name__ == "__main__":
    # Exemplo: Adicionar palavras ao banco
    inserir_palavra("cachorro", "substantivo")
    inserir_palavra("gato", "substantivo")
    inserir_palavra("corre", "verbo")
    inserir_palavra("rápido", "adjetivo")