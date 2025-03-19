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
    # Inserção massiva de palavras para um banco de dados mais robusto

    # 📌 Substantivos
    substantivos = [
        "cachorro", "gato", "homem", "mulher", "cidade", "carro", "avião", "praia", "computador", "telefone",
        "escola", "professor", "aluno", "livro", "janela", "porta", "relógio", "mesa", "cadeira", "banana",
        "futebol", "chuva", "sol", "lua", "tempo", "dinheiro", "trabalho", "floresta", "mar", "rio", "estrada",
        "montanha", "universidade", "empresa", "governo", "hospital", "igreja", "coração", "alma", "mente",
        "café", "chocolate", "música", "cinema", "teatro", "pintura", "escultura", "ciência", "tecnologia",
        "foguete", "robô", "planeta", "galáxia", "universo", "barco", "navio", "bicicleta", "motor",
        "ferramenta", "luz", "sombra", "caverna", "deserto", "história", "legenda", "mito", "costume",
        "amizade", "felicidade", "esperança", "saudade", "verdade", "mentira", "razão", "emoção", "arte"
    ]

    # 📌 Verbos
    verbos = [
        "corre", "anda", "pula", "fala", "come", "bebe", "estuda", "trabalha", "escreve", "lê",
        "viaja", "dirige", "canta", "dança", "joga", "nada", "dorme", "desenha", "ensina", "aprende",
        "grita", "sussurra", "ouve", "compra", "vende", "constrói", "derruba", "abraça", "beija", "olha",
        "acorda", "sonha", "planeja", "decide", "questiona", "responde", "explica", "descobre", "cria",
        "inova", "pensa", "esquece", "lembra", "procura", "encontra", "esconde", "revela", "pergunta",
        "resgata", "protege", "defende", "ataca", "vence", "perde", "celebra", "chora", "ri", "brinca",
        "explora", "investiga", "desenvolve", "constrói", "destrói", "desmonta", "monta", "organiza"
    ]

    # 📌 Adjetivos
    adjetivos = [
        "rápido", "devagar", "bonito", "feio", "grande", "pequeno", "forte", "fraco", "inteligente", "burro",
        "novo", "velho", "claro", "escuro", "rico", "pobre", "feliz", "triste", "alto", "baixo",
        "quente", "frio", "doce", "amargo", "macio", "duro", "limpo", "sujo", "leve", "pesado",
        "brilhante", "opaco", "longínquo", "próximo", "antigo", "moderno", "raro", "comum", "selvagem", "domesticado",
        "tímido", "extrovertido", "perigoso", "seguro", "audacioso", "cauteloso", "caro", "barato", "gentil", "grosseiro",
        "generoso", "egoísta", "humilde", "arrogante", "sensível", "insensível", "realista", "sonhador", "tranquilo", "nervoso",
        "lógico", "irracional", "otimista", "pessimista", "perfeito", "imperfeito", "misterioso", "transparente"
    ]

    # Inserir palavras no banco
    for palavra in substantivos:
        inserir_palavra(palavra, "substantivo")

    for palavra in verbos:
        inserir_palavra(palavra, "verbo")

    for palavra in adjetivos:
        inserir_palavra(palavra, "adjetivo")

    print("📌 Todas as palavras foram adicionadas ao banco de dados com sucesso!")
