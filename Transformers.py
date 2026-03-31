
from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")

#GPT-2

print("GPT-2: Gerando texto (Self-Attention)\n")
gpt2 = pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")

prompts = [
    "O avanço da inteligência artificial",
    "A ciência descobriu que",
    "O futuro da tecnologia é"
]

for p in prompts:
    print(f"Entrada: {p}")
    res = gpt2(p, max_new_tokens=40, do_sample=True, temperature=0.7, pad_token_id=50256)
    print(f"Continuação: {res[0]['generated_text'][len(p):]}\n")


#BERT

print("BERT: Preenchendo palavras escondidas ([MASK])\n")
bert = pipeline("fill-mask", model="neuralmind/bert-base-portuguese-cased")

frases = [
    "Lisboa é a capital de [MASK].",
    "O gato está em cima do [MASK]."
]

for f in frases:
    print(f"Frase: {f}")
    resultados = bert(f, top_k=3)
    for r in resultados:
        print(f"  {r['token_str']} | {r['score']:.2%}")
    print()


print("FIM")