# 🤖 Análise da Evolução da “Inteligência” em Chatbots

## 📌 Descrição do Projeto

Este projeto tem como objetivo analisar a evolução da **inteligência percebida em chatbots**, desde modelos baseados em regras até modelos modernos de **Processamento de Linguagem Natural (PLN)**.

Foram implementadas quatro abordagens diferentes:

* Fase 1: ELIZA (chatbot baseado em regras)
* Fase 2: N-Grams (modelo probabilístico)
* Fase 3: Word Embeddings (Word2Vec)
* Fase 4: Transformers (GPT-2 e BERT)

O trabalho busca demonstrar como cada técnica contribui para a simulação da linguagem humana e como a percepção de inteligência evolui ao longo das fases.

---

# 🎯 Objetivo

Desenvolver e analisar diferentes abordagens de construção de chatbots, comparando:

* capacidade de resposta
* coerência textual
* compreensão de linguagem
* percepção de inteligência
* limitações de cada modelo

---

# 🧠 Evolução das Fases

## 🔹 Fase 1 – ELIZA (Chatbot Baseado em Regras)

### 📖 Descrição

O ELIZA é um chatbot clássico baseado em regras e padrões de texto.

O sistema foi implementado em **Python** utilizando:

* Expressões Regulares (Regex)
* Dicionário de padrões
* Respostas pré-definidas
* Seleção aleatória de respostas

### ⚙️ Funcionamento

1. O usuário digita uma frase
2. O sistema procura padrões no texto
3. Se encontrar, retorna uma resposta
4. Caso não encontre, responde de forma genérica

### ✅ Vantagens

* Simples de implementar
* Simula conversação básica
* Baixo custo computacional
* Controle total das respostas

### ❌ Limitações

* Não entende o significado da frase
* Depende totalmente de padrões
* Respostas repetitivas
* Não aprende com o usuário
* Sem semântica

### 🧠 Inteligência percebida

Baixa — apenas simulação de conversa.

---

# 🔹 Fase 2 – N-Grams (Bigramas)

### 📖 Descrição

O modelo N-Gram utiliza **probabilidades de palavras** para gerar frases.

Foi implementado um **modelo de Bigramas**, onde cada palavra prevê a próxima.

### ⚙️ Funcionamento

1. Pré-processamento do texto
2. Tokenização das frases
3. Criação dos bigramas
4. Cálculo das probabilidades
5. Geração de texto

Exemplo:

```
você -> está -> bem
```

### ✅ Vantagens

* Gera texto automaticamente
* Mais flexível que ELIZA
* Usa estatística
* Melhora a coerência

### ❌ Limitações

* Depende do corpus
* Só olha 1 palavra anterior
* Não entende contexto
* Pode gerar frases sem sentido
* Problema de sparsidade

### 🧠 Inteligência percebida

Média — parece mais inteligente que ELIZA, mas ainda limitada.

---

# 🔹 Fase 3 – Word Embeddings (Word2Vec)

### 📖 Descrição

Nesta fase, as palavras são representadas como **vetores matemáticos**.

Foi utilizado:

* Gensim
* Word2Vec
* Skip-Gram
* PCA para visualização

### ⚙️ Funcionamento

1. Corpus de treinamento
2. Tokenização
3. Treinamento do Word2Vec
4. Vetores de palavras
5. Similaridade semântica

Exemplo:

```
python ≈ programação
django ≈ web
```

### 🧪 Operações possíveis

* Similaridade entre palavras
* Analogias
* Clusters semânticos
* Operações vetoriais

### ✅ Vantagens

* Entende semântica
* Palavras semelhantes ficam próximas
* Permite analogias
* Representação matemática da linguagem

### ❌ Limitações

* Vetor fixo por palavra
* Depende do corpus
* Não entende frase completa
* Não aprende sozinho

### 🧠 Inteligência percebida

Alta — já demonstra compreensão semântica.

---

# 🔹 Fase 4 – Transformers

### 📖 Descrição

Transformers são o **estado da arte em PLN**.

Utilizam:

* Self-Attention
* Contexto global
* Modelos pré-treinados
* Hugging Face

Foram utilizados:

* GPT-2 (geração de texto)
* BERT (preenchimento de lacunas)

---

## 🧪 GPT-2

Modelo:

```
pierreguillou/gpt2-small-portuguese
```

Função:

* gerar texto
* prever próxima palavra
* manter coerência

### Exemplo

Entrada:

```
O futuro da tecnologia é
```

Saída:

```
um caminho ao sucesso e ao crescimento da empresa
```

---

## 🧪 BERT

Modelo:

```
neuralmind/bert-base-portuguese-cased
```

Função:

* prever palavras faltantes
* entender contexto antes e depois

Exemplo:

```
Lisboa é a capital de [MASK]
```

Resultado:

```
Portugal (96%)
```

---

### ✅ Vantagens

* Entende contexto global
* Gera texto coerente
* Alta precisão
* Estado da arte
* Compreensão semântica avançada

### ❌ Limitações

* Alto custo computacional
* Precisa de modelos pré-treinados
* GPT pode gerar informação incorreta

### 🧠 Inteligência percebida

Muito alta — aproxima-se da linguagem humana.

---

# 📊 Comparação das Fases

| Fase         | Técnica        | Inteligência | Contexto | Semântica |
| ------------ | -------------- | ------------ | -------- | --------- |
| ELIZA        | Regras         | Baixa        | Não      | Não       |
| N-Grams      | Probabilidade  | Média        | Parcial  | Não       |
| Word2Vec     | Vetores        | Alta         | Parcial  | Sim       |
| Transformers | Self-Attention | Muito Alta   | Global   | Sim       |

---

# 🚀 Tecnologias Utilizadas

* Python
* Regex
* NLTK
* Gensim
* Scikit-learn
* Transformers
* Hugging Face
* GPT-2
* BERT

---

# 📌 Conclusão

O projeto demonstrou claramente a evolução dos chatbots ao longo do tempo.

* ELIZA simula conversa
* N-Grams usa probabilidade
* Word2Vec entende semântica
* Transformers entendem contexto global

Isso mostra que a inteligência percebida cresce conforme o modelo se torna mais complexo.

---

# 🧠 Impacto do RLHF

O uso de **Reinforcement Learning with Human Feedback (RLHF)** melhora ainda mais os Transformers, permitindo:

* respostas mais naturais
* alinhamento com humanos
* menos erros
* maior coerência

Assim, os modelos modernos representam o ponto mais avançado na evolução dos chatbots.

---

# 👨‍💻 Autores

Osvaldo Moura Neto
Mauro Antônio Pires
