import re
import random
from collections import defaultdict



CORPUS = """
oi tudo bem com você
estou bem e você
o que você está fazendo agora
estou estudando para a prova
você gosta de programação
sim eu muito de programação
qual linguagem você prefere
eu prefiro python e c mais uso c
você já fez algum projeto interessante
você já foi ao bar
sim estou fazendo um chatbot simples
isso parece muito legal
quando você vai terminar o projeto
acho que termino essa semana
você pode me ajudar com uma dúvida
claro qual é a sua dúvida
não entendi como funciona n gram
n gram usa probabilidade de palavras anteriores
entendi agora ficou mais claro
que bom fico feliz em ajudar
"""



def preprocessar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúâêîôûãõàç\s]", "", texto)

    frases = texto.strip().split("\n")

    frases_tokenizadas = []
    for frase in frases:
        palavras = frase.split()
        if palavras:
            palavras = ["<s>"] + palavras + ["</s>"]
            frases_tokenizadas.append(palavras)

    return frases_tokenizadas



def construir_bigramas(frases):
    modelo = defaultdict(list)

    for palavras in frases:
        for i in range(len(palavras) - 1):
            modelo[palavras[i]].append(palavras[i + 1])

    return modelo



def calcular_probabilidades(modelo):
    probabilidades = {}

    for palavra, sucessoras in modelo.items():
        total = len(sucessoras)
        contagem = defaultdict(int)

        for s in sucessoras:
            contagem[s] += 1

        probabilidades[palavra] = {
            s: contagem[s] / total
            for s in contagem
        }

    return probabilidades



def mostrar_probabilidades(probabilidades, palavra):
    if palavra not in probabilidades:
        print(f"\n[!] Palavra '{palavra}' não encontrada.\n")
        return

    print(f"\nDado '{palavra}', próxima palavra:")

    for proxima, prob in sorted(
        probabilidades[palavra].items(),
        key=lambda x: x[1],
        reverse=True
    ):
        barra = "█" * int(prob * 20)
        print(f"{proxima:<15} {barra} {prob * 100:.1f}%")



def gerar_texto(probabilidades, palavra_inicial="<s>", max_palavras=15):
    palavra_atual = palavra_inicial
    resultado = []

    for _ in range(max_palavras):
        if palavra_atual not in probabilidades:
            break

        proximas = list(probabilidades[palavra_atual].keys())
        probs = list(probabilidades[palavra_atual].values())

        palavra_atual = random.choices(proximas, weights=probs)[0]

        if palavra_atual == "</s>":
            break

        resultado.append(palavra_atual)

    return " ".join(resultado)



def demonstrar_limitacao(probabilidades):
    print("\nTextos CURTOS:")
    for _ in range(3):
        print("→", gerar_texto(probabilidades, "<s>", 6))

    print("\nTextos LONGOS:")
    for _ in range(3):
        print("→", gerar_texto(probabilidades, "<s>", 15))



def modo_interativo(probabilidades):
    print("\nDigite uma palavra ('sair' para encerrar)")

    while True:
        palavra = input("\nPalavra: ").strip().lower()

        if palavra == "sair":
            break

        mostrar_probabilidades(probabilidades, palavra)

        if palavra in probabilidades:
            print("Texto gerado:")
            print("→", gerar_texto(probabilidades, palavra))



if __name__ == "__main__":

    print("MODELO N-GRAM (BIGRAMA)\n")

    frases = preprocessar(CORPUS)
    modelo = construir_bigramas(frases)
    probabilidades = calcular_probabilidades(modelo)

    print("Exemplo de probabilidades:")
    mostrar_probabilidades(probabilidades, "você")
    mostrar_probabilidades(probabilidades, "estou")

    print("\nDemonstração da limitação do contexto:")
    demonstrar_limitacao(probabilidades)

    resp = input("\nEntrar no modo interativo? (s/n): ")
    if resp == "s":
        modo_interativo(probabilidades)

    print("\nFIM!")