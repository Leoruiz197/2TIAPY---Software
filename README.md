# README - Identificação de Verbos em Frases

## 1. Conjuntos de Palavras Auxiliares
O código inicia criando vários conjuntos de palavras que auxiliam na filtragem dos verbos:

- **NAO_VERBOS**: Contém palavras que não são verbos, como artigos ("o", "um"), preposições ("de", "em", "com") e determinantes ("meu", "seu").
- **PRONOMES**: Lista de pronomes pessoais ("eu", "tu", "ele").
- **MODAIS**: Lista de verbos auxiliares ("quero", "vou", "posso") que ajudam a prever sequências de verbos no infinitivo.
- **LINKING_VERBS**: Verbos de ligação ("sou", "estou", "era") que normalmente não indicam ações diretas.
- **SEPARADORES**: Palavras ou símbolos que separam frases ("e", "mas", ",", ";").

Essas listas são usadas para descartar palavras que não são verbos ou que influenciam a identificação.

## 2. Funções Auxiliares
As funções auxiliares verificam se uma palavra é um verbo com base em terminações comuns:

- **is_gerund(palavra)**: Verifica se a palavra termina em "ando", "endo" ou "indo", indicando que está no gerúndio (ex: "falando", "comendo").
- **is_infinitivo(palavra)**: Verifica se a palavra termina em "ar", "er" ou "ir", indicando que está no infinitivo (ex: "correr", "fazer").
- **eh_verbo_base(palavra)**:
  - Remove pontuações.
  - Descarta palavras das listas **NAO_VERBOS** e **PRONOMES**.
  - Confere se a palavra está no gerúndio, infinitivo ou tem terminações comuns de verbos conjugados ("eu corro", "eles falaram").

## 3. Função Principal: `identifica_verbos(frase)`
Essa função recebe uma frase e extrai os verbos dela. A lógica principal é:

1. Divide a frase em palavras.
2. Ignora palavras irrelevantes (artigos, preposições, pronomes).
3. Marca o início de novas cláusulas ao encontrar palavras como "para" ou separadores como "," e ";".
4. Identifica verbos seguindo estas regras:
   - O primeiro verbo em uma nova cláusula é aceito.
   - Se já houver um verbo na cláusula:
     - Se o último verbo era de ligação, só aceita o próximo se for gerúndio ou infinitivo.
     - Se o verbo anterior era modal, permite sequências como "vou correr" ou "posso treinar".
     - Se a palavra termina em uma conjugação comum ("ou", "ei"), é aceita como verbo.

## 4. Exemplo de Execução
Se rodarmos o código e inserirmos a frase:

```
Eu quero correr e depois vou nadar.
```

Ele identificará os verbos: **"quero", "correr", "vou", "nadar"**.

Explicação:
- **"quero"** está na lista de modais e inicia uma sequência de verbo no infinitivo ("correr").
- **"vou"** também está nos modais, permitindo o infinitivo "nadar".
- O **"e"** separa duas cláusulas, então "vou" inicia outra verificação.

## 5. Executando no Terminal
Se o código for executado em um terminal, ele pedirá uma frase ao usuário:

```
Digite uma frase:
> Eu preciso estudar e depois vou dormir.
```

E responderá:

```
Os verbos identificados são: ['preciso', 'estudar', 'vou', 'dormir']
```

## 6. Resumo
- Lista palavras irrelevantes (artigos, preposições, pronomes) para ignorá-las.
- Verifica terminações para saber se uma palavra é um verbo.
- Considera contexto: Se há verbos auxiliares ("vou", "posso"), permite sequências de infinitivos.
- Divide a frase e extrai os verbos, retornando apenas os relevantes.

Esse código é útil para análise de frases, ajudando a entender quais palavras indicam ações em um texto. 🚀

