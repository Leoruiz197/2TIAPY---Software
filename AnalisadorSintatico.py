import os

def carregar_verbos():
    """Carrega uma lista de verbos a partir de um arquivo externo."""
    verbos = set()
    caminho_arquivo = os.path.join(os.path.dirname(__file__), "verbos.txt")  # Caminho absoluto

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                verbo = linha.strip().lower()
                if verbo:  # Evita linhas vazias
                    verbos.add(verbo)
    except FileNotFoundError:
        print(f"⚠️ Arquivo 'verbos.txt' não encontrado no caminho: {caminho_arquivo}")
        print("Certifique-se de que o arquivo está na mesma pasta que o script.")
    
    return verbos

VERBOS_CONJUGADOS = carregar_verbos()

def limpar_texto(frase):
    """Remove pontuações manualmente e converte para minúsculas."""
    pontuacoes = ".,;:!()[]{}\"'`"
    frase_limpa = ""

    for char in frase:
        if char not in pontuacoes or char == "?":  # Mantemos "?" para perguntas
            frase_limpa += char

    return frase_limpa.lower()

def normalizar_nao(palavra):
    """Corrige erros comuns de digitação em 'não'."""
    variantes_nao = {"nao", "náo", "nâo", "nãp"}  # Possíveis erros
    return "não" if palavra in variantes_nao else palavra

def inferir_classe_gramatical(palavra):
    """
    Tenta inferir a classe gramatical de uma palavra baseada em padrões comuns.
    """
    palavra = normalizar_nao(palavra)  # Corrige variantes de "não"

    if palavra in VERBOS_CONJUGADOS:  # Verifica se a palavra está na lista de verbos carregada do arquivo
        return "verbo"
    elif palavra.endswith(("ar", "er", "ir", "ou", "ei", "ia", "eu", "am", "em")):  # Detecta conjugações comuns
        return "verbo"
    elif palavra.endswith(("mente")):  # Advérbios terminados em "mente"
        return "advérbio"
    elif palavra.endswith(("ção", "dade", "ismo", "ista")):  # Substantivos comuns
        return "substantivo"
    elif palavra in {"o", "a", "os", "as", "um", "uma"}:  # Artigos
        return "artigo"
    elif palavra in {"eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas"}:  # Pronomes pessoais
        return "pronome"
    elif palavra == "não":  # Qualquer variante normalizada será tratada corretamente
        return "negacao"
    elif palavra in {"para", "de", "com", "em", "por", "sobre", "contra", "pelo", "pela"}:  # Preposições
        return "preposição"
    else:
        return "possivel_substantivo"  # Assume que palavras desconhecidas podem ser substantivos próprios

def analisar_sintaxe(frase):
    """
    Analisa a estrutura da frase e identifica sujeito, verbo e complemento corretamente.
    """
    frase = limpar_texto(frase)
    palavras = frase.split()
    palavras = [normalizar_nao(p) for p in palavras]  # Normaliza "não" antes de classificar

    estrutura = {
        "sujeito": [],
        "verbo": None,
        "complemento": [],
        "tipo_frase": "declarativa"  # Default
    }

    encontrou_verbo = False
    sujeito_temp = []
    sujeito_nucleo = None  # Para armazenar o núcleo do sujeito
    negacao_encontrada = False  # Flag para capturar "não" e evitar que fique no sujeito

    for palavra in palavras:
        classe = inferir_classe_gramatical(palavra)

        if classe == "verbo":
            estrutura["verbo"] = palavra
            encontrou_verbo = True
        elif classe == "negacao":
            negacao_encontrada = True  # Marca que "não" foi encontrado
        elif not encontrou_verbo:
            sujeito_temp.append((palavra, classe))  # Armazena palavra + classe gramatical
        else:
            estrutura["complemento"].append(palavra)

    # Processar o sujeito garantindo que ele tenha núcleo (substantivo, pronome ou nome próprio)
    sujeito_final = []
    for i, (palavra, classe) in enumerate(sujeito_temp):
        if classe in ["substantivo", "possivel_substantivo", "pronome"]:
            sujeito_final.append(palavra)
            sujeito_nucleo = palavra
        elif classe == "artigo":
            # Se houver um substantivo logo após o artigo, não incluímos o artigo no sujeito
            if i + 1 < len(sujeito_temp) and sujeito_temp[i + 1][1] in ["substantivo", "possivel_substantivo"]:
                continue

    # Se o sujeito ainda está vazio e existe um substantivo identificado, mantemos o primeiro
    if not sujeito_final and sujeito_nucleo:
        sujeito_final.append(sujeito_nucleo)

    estrutura["sujeito"] = sujeito_final if sujeito_final else ["Não identificado"]

    # Se "não" foi encontrado, adicionamos no complemento
    if negacao_encontrada:
        estrutura["complemento"].insert(0, "não")

    # Ajusta o tipo de frase baseado no conteúdo
    if "?" in frase:
        estrutura["tipo_frase"] = "interrogativa"
    elif negacao_encontrada:
        estrutura["tipo_frase"] = "negativa"
    elif "foi" in palavras or "foram" in palavras:  # Frases passivas
        estrutura["tipo_frase"] = "passiva"

    return estrutura

# 🔹 Input do usuário 🔹
while True:
    frase_usuario = input("\nDigite uma frase para análise sintática (ou 'sair' para encerrar): ").strip()
    
    if frase_usuario.lower() == "sair":
        print("Encerrando o analisador sintático. Até mais! 👋")
        break

    resultado = analisar_sintaxe(frase_usuario)

    # Exibir resultado formatado
    print("\n📊 Resultado da análise sintática:")
    print(f"📌 Sujeito: {' '.join(resultado['sujeito'])}")
    print(f"📌 Verbo: {resultado['verbo']}")
    print(f"📌 Complemento: {' '.join(resultado['complemento']) if resultado['complemento'] else 'Nenhum'}")
    print(f"📌 Tipo de frase: {resultado['tipo_frase']}\n")
