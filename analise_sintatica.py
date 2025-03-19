import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('floresta')

from nltk.tokenize import word_tokenize
from nltk.corpus import floresta

# Treinar um modelo de etiquetagem baseado no corpus Floresta
tagger = nltk.UnigramTagger(floresta.tagged_sents())


def analisar_sintaxe(tokens):
    """Classifica as palavras e identifica a estrutura sintática"""
    tags = tagger.tag(tokens)
    estrutura = {
        "sujeito": [],
        "verbo": [],
        "complemento": [],
        "outros": []
    }

    for palavra, tag in tags:
        if not palavra:
            continue
        if tag and tag.startswith('N'):  # Substantivo
            estrutura["sujeito"].append(palavra)
        elif tag and tag.startswith('V'):  # Verbo
            estrutura["verbo"].append(palavra)
        elif tag and tag.startswith('A'):  # Adjetivo
            estrutura["complemento"].append(palavra)
        else:
            estrutura["outros"].append(palavra)

    return estrutura


if __name__ == "__main__":
    frase = "O cachorro corre rápido pelo parque."
    tokens = word_tokenize(frase, language="portuguese")
    analise = analisar_sintaxe(tokens)

    print("Análise Sintática:", analise)