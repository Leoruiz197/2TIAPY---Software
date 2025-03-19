# Conjunto de palavras que geralmente não são verbos (determinantes, preposições, etc.)
NAO_VERBOS = {
    "meu", "minha", "seu", "sua", "teu", "tua",
    "nosso", "nossa", "vossos", "vossa",
    "o", "a", "os", "as", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "com", "por", "para", "após", "sem", "sobre"
}

# Pronomes pessoais
PRONOMES = {"eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas", "você", "vocês"}

# Verbos auxiliares/modais (para identificar sequências em infinitivo)
MODAIS = {"quero", "vou", "posso", "devo", "preciso"}

# Verbos de ligação (ser, estar, etc.) – quando aceitos, o token seguinte tende a ser complemento
LINKING_VERBS = {
    "sou", "és", "é", "somos", "são", "fui", "foi", "fomos", "foram",
    "estou", "está", "estamos", "estão", "estava", "estavam", "estive", "estivemos", "estiveram",
    "era", "eram"
}

# Palavras que separam cláusulas
SEPARADORES = {"e", "mas", "ou", "porém", ",", ";", ":", "–"}

def is_gerund(palavra):
    """
    Retorna True se a palavra estiver na forma de gerúndio (termina em "ando", "endo" ou "indo").
    """
    palavra = palavra.lower().strip(".,;!?")
    return palavra.endswith(("ando", "endo", "indo"))

def is_infinitivo(palavra):
    """
    Retorna True se a palavra estiver na forma infinitiva (termina em "ar", "er" ou "ir").
    """
    palavra = palavra.lower().strip(".,;!?")
    return palavra.endswith(("ar", "er", "ir"))

def eh_verbo_base(palavra):
    """
    Verifica se a palavra pode ser considerada um verbo com base em regras simples de terminação.
    Aplica filtros para artigos, preposições e pronomes.
    Inclui verificação para infinitivos, gerúndios e algumas terminações comuns de verbos conjugados.
    """
    palavra = palavra.lower().strip(".,;!?")
    if palavra in NAO_VERBOS or palavra in PRONOMES:
        return False
    # Reconhece gerúndio
    if is_gerund(palavra):
        return True
    # Reconhece infinitivo
    if palavra.endswith(("ar", "er", "ir")):
        return True
    # Verifica terminações comuns de formas conjugadas
    terminações = ("o", "as", "a", "amos", "am", "e", "em", "ei", "ou",
                   "aram", "eram", "iram", "iste", "iu", "eu")
    if palavra.endswith(terminações):
        return True
    return False

def identifica_verbos(frase):
    """
    Recebe uma frase e retorna uma lista com os tokens identificados como verbos,
    utilizando heurísticas de terminação e contexto.
    
    Estratégia:
      - Divide a frase em tokens usando espaços.
      - Tokens que são artigos, preposições ou pronomes são ignorados.
      - Se um token é "para", ele é tratado como marcador de início de nova cláusula.
      - Se um token é o primeiro de uma cláusula (após separadores ou marcador especial), ele é aceito como verbo.
      - Se já houver um verbo na cláusula:
           * Apenas tokens em forma infinitiva ou de gerúndio serão aceitos.
           * Se o último verbo aceito for um verbo de ligação, a ideia é que o próximo token seja um complemento,
             então só aceitaremos se ele for infinitivo ou gerúndio.
           * Para infinitivos, se o verbo imediatamente anterior também for infinitivo (ou estiver em MODAIS), 
             o token é aceito, permitindo sequências como "ir treinar" ou "fazer digestão".
    """
    tokens = frase.split()
    verbos = []
    new_clause = True  # Indicador de início de cláusula
    ultimo_verbo = None  # Armazena o último token aceito como verbo (em minúsculas)
    
    for i, token in enumerate(tokens):
        token_limpo = token.lower().strip(".,;!?")
        
        # Se o token é um separador, reinicia o indicador de nova cláusula.
        if token_limpo in SEPARADORES:
            new_clause = True
            continue
        
        # Tratamento especial: se o token for "para", assume início de nova cláusula e o ignora.
        if token_limpo == "para":
            new_clause = True
            continue
        
        # Ignora tokens que são artigos, preposições ou pronomes.
        if token_limpo in NAO_VERBOS or token_limpo in PRONOMES:
            continue
        
        # Se o token anterior for um desses termos, pula o token atual.
        if i > 0:
            prev = tokens[i-1].lower().strip(".,;!?")
            if prev in NAO_VERBOS:
                continue
        
        if eh_verbo_base(token):
            if new_clause:
                # Se é o primeiro token da cláusula, aceita como verbo.
                verbos.append(token)
                new_clause = False
                ultimo_verbo = token_limpo
            else:
                # Se o último verbo aceito for de ligação, só aceita se o token atual for infinitivo ou gerúndio.
                if ultimo_verbo in LINKING_VERBS:
                    if not (is_infinitivo(token) or is_gerund(token)):
                        continue
                    else:
                        verbos.append(token)
                        ultimo_verbo = token_limpo
                        continue
                # Se o token está em forma infinitiva, permite o encadeamento se o verbo anterior for modal ou também estiver em infinitivo.
                if is_infinitivo(token):
                    if ultimo_verbo in MODAIS or is_infinitivo(ultimo_verbo):
                        verbos.append(token)
                        ultimo_verbo = token_limpo
                    else:
                        continue
                # Se o token é gerúndio, aceita-o.
                elif is_gerund(token):
                    verbos.append(token)
                    ultimo_verbo = token_limpo
                else:
                    # Caso seja outra forma conjugada e já exista um verbo na cláusula, é provável que seja complemento.
                    continue
    return verbos

if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    verbos_encontrados = identifica_verbos(frase)
    print("Os verbos identificados são:", verbos_encontrados)
 