import string

ARTIGOS = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']
PRONOMES = ['ele', 'ela', 'eles', 'elas', 'nós', 'vós', 'me', 'te', 'se', 'nos', 'vos', 'lhe', 'lhes', 'meu', 'minha',
            'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'seu', 'sua', 'seus', 'suas', 'nosso', 'nossa', 'nossos',
            'nossas', 'vosso', 'vossa', 'vossos', 'vossas', 'este', 'esta', 'estes', 'estas', 'esse', 'essa', 'esses',
            'essas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'isso', 'aquilo', 'alguém', 'ninguém', 'outrem',
            'algo', 'nada', 'tudo', 'cada', 'qualquer', 'quem', 'que', 'cujo', 'cuja', 'cujos', 'cujas', 'onde',
            'quando', 'como', 'porque', 'quanto', 'quanta', 'quantos', 'quantas', 'qual', 'quais']

def limpar_tokens(tokens):
    ultima_palavra = tokens[-1]
    ultimo_caracter = ultima_palavra[-1]
    if ultimo_caracter in string.punctuation:
        tokens[-1] = ultima_palavra[:-1]
    return tokens

def carregar_verbos(prefixo):
    arquivo = f'verbos/{prefixo}.txt'
    try:
        with open(arquivo) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def extraia_predicado(frase):
    tokens = [token.strip() for token in frase.lower().split()]
    tokens = limpar_tokens(tokens)

    for token in tokens:
        if len(token) < 3 or token in PRONOMES:
            continue

        verbos = carregar_verbos(token[:2])
        if token in verbos:
            index = tokens.index(token)
            if index > 0 and tokens[index - 1] in ARTIGOS:
                continue
            return ' '.join(tokens[index:])

    return ' '.join(tokens)