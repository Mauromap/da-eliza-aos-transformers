"""
Fase 2: Predição por N-Grams (Bigramas)
Atividade: Da ELIZA aos Transformers

Conceito:
  - Bigrama = N-Gram com N=2
  - A probabilidade da próxima palavra é calculada
    com base apenas na palavra ANTERIOR (n-1).
  - Isso é chamado de Modelo de Markov de 1ª ordem.
"""

import re
import random
from collections import defaultdict


# ==================================================
# 1. CORPUS DE TREINAMENTO
# Frases de exemplo em português
# ==================================================

CORPUS = """
o gato miou muito alto
o gato correu pelo jardim
o cachorro latiu para o gato
o cachorro dormiu no tapete
o menino brincou com o cachorro
o menino comeu o pão
a menina cantou uma música bonita
a menina correu pelo parque
a música tocou muito alto
o pão ficou frio na mesa
o jardim ficou verde depois da chuva
a chuva caiu muito forte
o sol brilhou depois da chuva
a casa ficou molhada com a chuva
o livro ficou em cima da mesa
a mesa ficou suja com o pão
o computador processou os dados muito rápido
os dados foram analisados pelo computador
a linguagem natural é processada pelo computador
o modelo aprendeu com os dados de treinamento
"""


# ==================================================
# 2. PRÉ-PROCESSAMENTO DO TEXTO
# ==================================================

def preprocessar(texto):
    """
    Limpa e tokeniza o texto.
    Retorna uma lista de palavras em minúsculas.
    """
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúâêîôûãõàç\s]", "", texto)
    palavras = texto.split()
    return palavras


# ==================================================
# 3. CONSTRUÇÃO DO MODELO DE BIGRAMAS
# ==================================================

def construir_bigramas(palavras):
    """
    Cria um dicionário de bigramas.
    Para cada palavra, guarda uma lista de palavras
    que aparecem logo depois dela no corpus.

    Estrutura: { "palavra_atual": ["próxima1", "próxima2", ...] }
    """
    modelo = defaultdict(list)

    for i in range(len(palavras) - 1):
        palavra_atual = palavras[i]
        proxima_palavra = palavras[i + 1]
        modelo[palavra_atual].append(proxima_palavra)

    return modelo


# ==================================================
# 4. CÁLCULO DE PROBABILIDADE
# ==================================================

def calcular_probabilidades(modelo):
    """
    Para cada palavra, conta a frequência de cada
    sucessora e calcula a probabilidade.

    Retorna: { "palavra": {"próxima": probabilidade} }
    """
    probabilidades = {}

    for palavra, sucessoras in modelo.items():
        total = len(sucessoras)
        contagem = defaultdict(int)

        for s in sucessoras:
            contagem[s] += 1

        probabilidades[palavra] = {
            s: round(contagem[s] / total, 4)
            for s in contagem
        }

    return probabilidades


# ==================================================
# 5. GERAÇÃO DE TEXTO
# ==================================================

def gerar_texto(modelo, palavra_inicial, num_palavras=10):
    """
    Gera uma sequência de palavras usando o modelo
    de bigramas. A cada passo, escolhe aleatoriamente
    a próxima palavra com base nas probabilidades.
    """
    resultado = [palavra_inicial]
    palavra_atual = palavra_inicial

    for _ in range(num_palavras - 1):
        if palavra_atual not in modelo:
            break  # Sem continuação conhecida
        proximas = modelo[palavra_atual]
        palavra_atual = random.choice(proximas)
        resultado.append(palavra_atual)

    return " ".join(resultado)


# ==================================================
# 6. EXIBIÇÃO DIDÁTICA DAS PROBABILIDADES
# ==================================================

def exibir_probabilidades(probabilidades, palavra):
    """
    Mostra as probabilidades da próxima palavra
    dado uma palavra de entrada. Igual ao slide
    do exemplo 'O gato...'
    """
    if palavra not in probabilidades:
        print(f"\n[!] Palavra '{palavra}' não encontrada no corpus.\n")
        return

    print(f"\nDado '{palavra}', as probabilidades são:")
    print("-" * 40)

    # Ordena da maior para menor probabilidade
    for proxima, prob in sorted(
        probabilidades[palavra].items(),
        key=lambda x: x[1],
        reverse=True
    ):
        barra = "█" * int(prob * 30)
        print(f"  {proxima:<15} {barra} {prob * 100:.1f}%")
    print()


# ==================================================
# 7. EXECUÇÃO PRINCIPAL
# ==================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  MODELO DE N-GRAMS — BIGRAMAS (N=2)")
    print("  Fase 2: Da ELIZA aos Transformers")
    print("=" * 50)

    # Pré-processamento
    palavras = preprocessar(CORPUS)
    print(f"\nCorpus carregado: {len(palavras)} palavras.\n")

    # Construção do modelo
    modelo = construir_bigramas(palavras)
    probabilidades = calcular_probabilidades(modelo)

    # --- Exemplo do slide: "O gato..." ---
    exibir_probabilidades(probabilidades, "gato")
    exibir_probabilidades(probabilidades, "o")
    exibir_probabilidades(probabilidades, "a")

    # --- Geração de texto ---
    print("Textos gerados pelo modelo:\n")
    palavras_iniciais = ["o", "a", "o", "a", "o"]

    for inicio in palavras_iniciais:
        texto = gerar_texto(modelo, inicio, num_palavras=8)
        print(f"  → {texto}")

    print()
    print("=" * 50)
    print("REFLEXÃO:")
    print("  O modelo só enxerga 1 palavra atrás.")
    print("  Por isso, frases longas perdem coerência.")
    print("  Trigramas melhorariam, mas o problema")
    print("  de contexto curto continuaria existindo.")
    print("=" * 50)