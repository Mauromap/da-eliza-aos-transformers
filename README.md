# 📚 Da ELIZA aos Transformers — Guia de Execução

## Estrutura do Projeto

```
projeto/
│
├── fase1_eliza.py              ← Chatbot ELIZA com Regex (já feito)
├── fase2_ngrams.py             ← Predição por N-Grams (já feito)
├── fase3_word_embeddings.py    ← Word Embeddings com Word2Vec  ← NOVO
└── fase4_transformers.py       ← Transformers GPT-2 e BERT     ← NOVO
```

---

## ⚙️ Instalação das Dependências

Abra o terminal (ou o terminal integrado do VS Code) e rode:

```bash
# Fase 3 — Word Embeddings
pip install gensim

# Fase 4 — Transformers
pip install transformers torch
```

> 💡 **Dica:** Se der erro de permissão, tente `pip install --user gensim`

---

## ▶️ Como Executar

### Fase 3 — Word Embeddings
```bash
python fase3_word_embeddings.py
```
**O que você vai ver:**
- A palavra "gato" representada como lista de números (vetor)
- As palavras mais similares a "rei", "gato", "homem", etc.
- A operação: **REI - HOMEM + MULHER = RAINHA** 🪄
- Comparação de similaridade entre pares de palavras

---

### Fase 4 — Transformers
```bash
python fase4_transformers.py
```
**⚠️ Na primeira execução:** Os modelos serão baixados automaticamente (~500MB). Isso é normal e ocorre apenas uma vez.

**O que você vai ver:**
- **GPT-2** completando frases automaticamente
- **BERT** adivinhando palavras escondidas `[MASK]`
- **Análise de sentimento** detectando emoção em textos
- Comparativo completo das 4 fases

---

## 💡 Resumo do que cada fase ensina

| Fase | Técnica | Ideia Central | Limitação |
|------|---------|---------------|-----------|
| 1 — ELIZA | Regex / Regras | Respostas fixas por palavras-chave | Fora do roteiro = falha |
| 2 — N-Grams | Probabilidade | Frequência dita a próxima palavra | Contexto curto (2-3 palavras) |
| 3 — Word2Vec | Vetores | Palavras como pontos no espaço | Uma palavra = um vetor fixo |
| 4 — Transformers | Self-Attention | Contexto dinâmico da frase inteira | Precisa de muito poder computacional |

---

## 🔑 Conceitos-Chave para o Relatório

### Fase 3 — Word Embeddings
- **Word2Vec:** algoritmo que transforma palavras em vetores numéricos
- **Espaço Vetorial:** "mapa" onde palavras similares ficam próximas
- **Similaridade por Cosseno:** mede o ângulo entre dois vetores (0 = diferente, 1 = idêntico)
- **Álgebra Vetorial:** REI - HOMEM + MULHER = RAINHA

### Fase 4 — Transformers
- **Self-Attention:** mecanismo que permite ao modelo "focar" nas partes mais importantes da frase
- **Processamento Paralelo:** diferente das RNNs (que processavam palavra por palavra), os Transformers processam a frase inteira de uma vez
- **BERT:** modelo bidirecional — lê a frase para frente e para trás
- **GPT-2:** modelo autoregressive — gera texto da esquerda para a direita
- **RLHF:** técnica usada para alinhar modelos como o ChatGPT com preferências humanas

---

## 📝 Estrutura Sugerida para o Relatório

1. **Introdução** — Apresentar a jornada das 4 fases
2. **Fase 1** — ELIZA: rigidez dos sistemas de regras
3. **Fase 2** — N-Grams: a emergência da estatística
4. **Fase 3** — Word2Vec: palavras como matemática
5. **Fase 4** — Transformers: a revolução da atenção
6. **Comparativo** — Tabela com Lógica / Contexto / Flexibilidade
7. **Conclusão** — Impacto do RLHF no resultado final (ChatGPT, Claude, etc.)
"# da-eliza-aos-transformers" 
# da-eliza-aos-transformers
