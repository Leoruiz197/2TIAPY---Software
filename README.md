# 📝 2TIAPY-GRUPO-01-Software

## 📖 Roteiro para Desenvolvimento de um Projeto de NLP sem Bibliotecas Prontas

### 👥 Equipe

A equipe é composta por quatro integrantes:

- **Alan de Souza Maximiano da Silva** | 📧 [rm557088@fiap.com.br](mailto:rm557088@fiap.com.br)
- **Paulo Carvalho Ruiz Borba** | 📧 [rm554562@fiap.com.br](mailto:rm554562@fiap.com.br)
- **Lancelot Chagas Rodrigues** | 📧 [rm554707@fiap.com.br](mailto:rm554707@fiap.com.br)
- **Mizael Vieira Bezerra** | 📧 [rm555796@fiap.com.br](mailto:rm555796@fiap.com.br)

---

## 🎯 1. Objetivo do Projeto

Criar um sistema básico de **Processamento de Linguagem Natural (NLP)** do zero, sem o uso de bibliotecas externas de NLP. O sistema terá as seguintes funcionalidades:

✅ **Tokenizar frases** (separar palavras em unidades de significado).  
✅ **Identificar classes gramaticais** (substantivo, verbo, adjetivo etc.).  
✅ **Analisar a estrutura da sentença** (identificação de sujeito, verbo e complemento).  
✅ **Armazenar frases processadas** para futuras consultas.  
✅ **Fornecer uma interface intuitiva** para interação com o sistema.  
✅ **Utilizar um banco de dados para armazenar palavras e regras gramaticais**.  

---

## 🏗️ 2. Funcionamento do Código

O projeto é modular e segue um fluxo bem definido:

1️⃣ **Tokenização e Pré-processamento**  
   - Normaliza a frase (remoção de pontuação, conversão para minúsculas).  
   - Divide a frase em palavras (tokens).  
   - Remove stopwords irrelevantes.

2️⃣ **Análise Sintática**  
   - Classifica palavras como substantivo, verbo ou adjetivo.  
   - Identifica a estrutura da frase (sujeito, verbo e complemento).  
   - Utiliza regras manuais armazenadas no banco de dados.

3️⃣ **Armazenamento e Recuperação**  
   - Frases processadas são armazenadas em um banco SQLite.  
   - Possibilita consulta e aprendizado contínuo.

4️⃣ **Interface Web (Streamlit)**  
   - Exibe os resultados do processamento e métricas da análise.  
   - Facilita interação com os dados armazenados.

---

## 🚀 3. Inovações e Benefícios do Banco de Dados

A principal inovação é o uso de um **banco de dados** para gerenciar palavras e frases analisadas. Isso traz diversos benefícios:

✅ **Expansibilidade** → Permite adicionar **novas palavras** sem alterar o código.  
✅ **Eficiência** → Evita reprocessamento ao consultar frases já analisadas.  
✅ **Aprendizado Contínuo** → Permite refinamento de regras gramaticais com base em novos dados.  
✅ **Otimização** → Consulta rápida para identificar padrões linguísticos.  
✅ **Personalização** → Possibilita ajustes personalizados na análise sintática.  

---

## 🛠️ 4. Divisão da Equipe e Tarefas

### 📌 **Paulo - Tokenização e Pré-processamento**
- Criar um **tokenizador** para segmentar frases em palavras.
- Implementar **normalização de texto** (remoção de pontuações, conversão para minúsculas).
- Desenvolver um **removedor de stopwords** (eliminação de palavras irrelevantes).

### 📌 **Mizael - Analisador Sintático**
- Criar um **sistema básico de classificação gramatical** (substantivo, verbo, adjetivo etc.).
- Implementar um **parser sintático** para identificar a estrutura das frases.
- Definir **regras para reconhecer sujeito, verbo e complemento**.

### 📌 **Lancelot - Banco de Dados e Armazenamento**
- Criar um **sistema de armazenamento** para salvar frases e análises.
- Implementar **indexação e recuperação** de frases analisadas.
- Criar um **mecanismo para armazenar regras gramaticais** definidas manualmente.

### 📌 **Alan - Interface e Integração**
- Criar uma **interface simples (CLI ou Web)** para entrada de frases e exibição dos resultados.
- **Integrar os módulos** desenvolvidos pelos demais integrantes.
- **Realizar testes e corrigir erros** de integração.
- **Gerenciar a documentação** e manter o repositório atualizado no **GitHub**.

---

## 📅 5. Cronograma de Desenvolvimento

### 📌 **Primeira Semana**
🔹 **Quarta-feira - Aula 01 (1h30min)**  
✅ Definição do **escopo e divisão das tarefas**.  
✅ Configuração inicial do projeto e **estruturação dos arquivos**.  
✅ Início do desenvolvimento **individual de cada módulo**.  

🔹 **Quarta-feira - Aula 02 (1h30min)**  
✅ Desenvolvimento dos módulos individuais.  
✅ Primeiros testes com frases simples.  
✅ Ajustes e refinamento dos algoritmos.

---

### 📌 **Segunda Semana**
🔹 **Quarta-feira - Aula 03 (1h30min)**  
✅ **Integração dos módulos criados**.  
✅ Testes com **frases reais** e identificação de **possíveis erros**.  
✅ Melhorias na **análise sintática** e refinamento das **regras gramaticais**.  

🔹 **Quarta-feira - Aula 04 (1h30min)**  
✅ **Otimização do código** e testes finais.  
✅ **Documentação e apresentação** do projeto concluído.  

---

## ⚠️ 6. Regras e Restrições

✅ **Não usar bibliotecas de NLP** como NLTK, Spacy, etc.  
✅ **Implementação do zero** de tokenização, parsing e análise sintática.  
✅ **Código modular e reutilizável** para futuras expansões.  
✅ **Manutenção da documentação** atualizada até a finalização do projeto.  
✅ **Uso de banco de dados** para otimizar armazenamento e recuperação de frases.  

---

## 🚀 7. Como Executar o Projeto

### 🔹 **1. Clone o Repositório**
```bash
git clone https://github.com/alansms/2TIAPY-GRUPO-01-Software.git
cd 2TIAPY-GRUPO-01-Software
```

### 🔹 **2. Configure o Banco de Dados**
Antes de rodar a aplicação, crie as tabelas executando:
```bash
python database.py
```

### 🔹 **3. Execute a Interface Web**
```bash
streamlit run app.py
```

Agora, basta **digitar uma frase**, processá-la e visualizar os resultados diretamente no navegador! 🚀

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
