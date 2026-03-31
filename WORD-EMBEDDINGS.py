import re
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# ------------------------
# 1️⃣ Corpus em português
# ------------------------
CORPUS = """
oi tudo bem com você
estou bem e você
o que você está fazendo agora
estou estudando para a prova
você gosta de programação
sim eu gosto muito de programação
qual linguagem você prefere
eu gosto de python
programação é divertida
estudar python é interessante
python é uma linguagem de programação
python é muito fácil de aprender
programação com python é incrível
desenvolvimento web usa python
ciência de dados usa python
inteligência artificial usa python
python tem uma comunidade grande
eu amo programação e desenvolvimento
programar é meu hobby favorito
código bem escrito é importante
ferramentas de programação python
aprender python é fácil e divertido
python para web é django
python para dados é pandas
python para máquina é scikit
desenvolvimento é importante
código limpo é fundamental
algoritmos são a base da programação
estrutura de dados é essencial
sistema operacional é importante
banco de dados é fundamental
servidor web é necessário
aplicação mobile é moderna
web design é criativo
programador trabalha com código
desenvolvedor cria soluções
engenheiro de software resolve problemas
computador executa programas
processador é veloz
memória é importante
algoritmo eficiente é rápido
código lento é problema
compilador converte código
linguagem python é popular
javascript é para web
java é poderosa
c é rápida
compilar código é necessário
executar programa funciona bem
testar código é importante
bugs são problemas
debug é solução
erro de lógica é comum
sintaxe incorreta é erro
função encapsula código
classe define objeto
objeto tem propriedades
propriedade armazena valor
método executa ação
return retorna valor
loop repete ação
condição toma decisão
if else escolhe caminho
while repete enquanto
for repete para tudo
lista armazena dados
dicionário armazena pares
conjunto elimina duplicatas
tupla é imutável
string é texto
número é inteiro
decimal é float
caractere é letra
arquivo salva dados
arquivo lê dados
json é formato
xml é estrutura
banco relacional organiza
sql consulta banco
query busca informação
resultado retorna dados
conexão liga sistemas
rede conecta computadores
internet liga mundo
servidor serve dados
cliente pede dados
requisição envia pedido
resposta recebe dados
"""

# ------------------------
# 2️⃣ Pré-processamento simples
# ------------------------
def preprocess(texto):
    texto = texto.lower()  # tudo minúsculo
    texto = re.sub(r'[^a-záéíóúãõç\s]', '', texto)  # remove caracteres especiais
    return [linha.split() for linha in texto.strip().split("\n")]

sentencas = preprocess(CORPUS)
print("Sentenças tokenizadas:")
print(sentencas)

# ------------------------
# 3️⃣ Treinar Word2Vec
# ------------------------
modelo = Word2Vec(
    sentences=sentencas,
    vector_size=50,
    window=3,
    min_count=1,
    sg=1,
    workers=2
)

# ------------------------
# 4️⃣ Palavras mais similares
# ------------------------
palavras_chave = ['programação', 'python', 'estudar']

for palavra in palavras_chave:
    similares = modelo.wv.most_similar(palavra, topn=5)
    print(f"\nPalavras mais similares a '{palavra}':")
    for s, score in similares:
        print(f"  {s} (similaridade: {score:.2f})")

# ------------------------
# 5️⃣ Similaridade entre pares
# ------------------------
sim = modelo.wv.similarity('programação', 'python')
print(f"\nSimilaridade entre 'programação' e 'python': {sim:.2f}")

# ------------------------
# 6️⃣ OPERAÇÕES VETORIAIS COM ANALOGIAS
# ------------------------
print("\n" + "="*60)
print("OPERAÇÕES VETORIAIS - ANALOGIAS QUE FAZEM SENTIDO")
print("="*60)

print("""
Conceito: Você pode combinar vetores de palavras para encontrar
relações semânticas! 

Fórmula: vetor_resultado = vetor_A + vetor_B - vetor_C

Exemplos práticos de analogias:
  • python + web = ? (linguagem + contexto)
  • programação - dificuldade + diversão = ? (mudando sentimento)
  • aprender + python = ? (combinar ações com objetos)
""")

# Lista de operações que fazem sentido
operacoes = [
    {
        'nome': 'Linguagem + Web',
        'positive': ['python', 'web'],
        'negative': [],
        'descricao': 'Que palavra está perto de "python" e "web"?'
    },
    {
        'nome': 'Programação - Difícil + Diversão',
        'positive': ['programação', 'diversão'],
        'negative': ['difícil'] if 'difícil' in modelo.wv else [],
        'descricao': 'Programação sem dificuldade, mas com diversão = ?'
    },
    {
        'nome': 'Python + Acelerado',
        'positive': ['python', 'bem'],
        'negative': [],
        'descricao': 'Python em bom contexto/sentimento = ?'
    },
    {
        'nome': 'Estudo + Python',
        'positive': ['estudar', 'python'],
        'negative': [],
        'descricao': 'Estudar sobre Python = ?'
    }
]

print("\nExecutando operações vetoriais:\n")
for op in operacoes:
    print(f"[{op['nome']}]")
    print(f"  Pergunta: {op['descricao']}")
    
    # Filtra palavras que realmente existem no modelo
    positive = [p for p in op['positive'] if p in modelo.wv]
    negative = [n for n in op['negative'] if n in modelo.wv]
    
    if positive:  # Só executa se houver palavras válidas
        try:
            resultados = modelo.wv.most_similar(
                positive=positive,
                negative=negative,
                topn=3
            )
            
            print(f"  Fórmula: {' + '.join(positive)}", end="")
            if negative:
                print(f" - {' - '.join(negative)}", end="")
            print(" = ?")
            
            print("  Resultados:")
            for i, (palavra, score) in enumerate(resultados, 1):
                barra = "█" * int(score * 20)
                print(f"    {i}. {palavra:15} {barra} {score:.3f}")
        except Exception as e:
            print(f"  Erro: {str(e)[:50]}")
    else:
        print(f"  Palavras não encontradas no corpus")
    print()

# Operação especial: ANALOGIA CLÁSSICA
print("-" * 60)
print("ANALOGIA CLÁSSICA: A está para B assim como C está para D")
print("-" * 60)
print("""
No Word2Vec clássico:
  KING - MAN + WOMAN ≈ QUEEN
  
Em português, um exemplo similar seria:
  PYTHON - INICIANTE + AVANÇADO ≈ ?
  
Lógica: Se python está para "fácil", então 
        qual palavra está para "difícil"?
""")

try:
    # Tenta encontrar uma analogia significativa
    resultado = modelo.wv.most_similar(
        positive=['python', 'avançado'] if 'avançado' in modelo.wv else ['python', 'bem'],
        negative=['iniciante'] if 'iniciante' in modelo.wv else [],
        topn=3
    )
    
    if resultado:
        print("Top 3 Palavras encontradas:")
        for i, (palavra, score) in enumerate(resultado, 1):
            print(f"  {i}. {palavra:15} (score: {score:.3f})")
except:
    print("  [Não foi possível realizar a analogia]")

# EXPLICAÇÃO VISUAL DE COMO FUNCIONA
print("\n" + "="*60)
print("COMO FUNCIONA MATEMATICAMENTE")
print("="*60)

print("""
1. CADA PALAVRA = UM VETOR (lista de números)
   Exemplo: python = [0.12, -0.45, 0.78, 0.23, ...]
   
2. PALAVRAS SIMILARES TÊM VETORES PRÓXIMOS
   ┌─────────────┐
   │   Espaço    │
   │  Vetorial   │  • programação ← perto
   │             │  • python      ← perto
   │ (50 dims)   │  • código      ← distante
   │             │  • gato        ← MUITO distante
   └─────────────┘

3. OPERAÇÕES VETORIAIS = ÁLGEBRA LINEAR
   V(python) + V(web) - V(fácil) = V(?)
   
   O modelo busca qual palavra fica perto desse ponto!

4. EXEMPLOS DO MUNDO REAL:
   • V(Rei) - V(Homem) + V(Mulher) ≈ V(Rainha) ✓
   • V(Paris) - V(França) + V(Brasil) ≈ V(Brasília) ✓
   • V(Python) - V(Web) + V(Desktop) ≈ V(? ) ?
""")

# MOSTRA OS VETORES REAIS DE ALGUMAS PALAVRAS
print("\nVETORES REAIS DE ALGUMAS PALAVRAS:")
print("-" * 60)

for palavra in ['python', 'programação', 'estudar']:
    if palavra in modelo.wv:
        vetor = modelo.wv[palavra]
        print(f"\n'{palavra}':")
        print(f"  Primeiros 10 valores: {vetor[:10]}")
        print(f"  Magnitude (tamanho): {sum(v**2 for v in vetor)**0.5:.3f}")
        print(f"  Dimensão total: 50 valores")

# FUNÇÃO PARA TESTAR OPERAÇÕES CUSTOMIZADAS
print("\n" + "="*60)
print("TESTADOR DE OPERAÇÕES CUSTOMIZADAS")
print("="*60)

def testar_operacao(positive, negative, descricao):
    """Testa uma operação vetorial e mostra os melhores resultados."""
    print(f"\n[{descricao}]")
    
    # Filtra apenas palavras que existem
    p_validas = [x for x in positive if x in modelo.wv]
    n_validas = [x for x in negative if x in modelo.wv]
    
    if not p_validas:
        print("  Nenhuma palavra positiva encontrada no modelo!")
        return
    
    try:
        resultado = modelo.wv.most_similar(
            positive=p_validas,
            negative=n_validas,
            topn=5
        )
        
        print(f"  Entrando: {' + '.join(p_validas)}", end="")
        if n_validas:
            print(f" - {' - '.join(n_validas)}", end="")
        print(" = ?")
        print("\n  Top 5 resultados:")
        
        for i, (palavra, cosine_sim) in enumerate(resultado, 1):
            barra = "█" * int(cosine_sim * 25)
            print(f"    {i}. {palavra:15} {barra} {cosine_sim:.4f}")
    
    except Exception as e:
        print(f"  Erro: {e}")

# Testa algumas operações
testar_operacao(['python'], [], "Similares a PYTHON")
testar_operacao(['programação', 'bem'], [], "PROGRAMAÇÃO + BEM")
testar_operacao(['python', 'estudar'], [], "PYTHON + ESTUDAR")

# RESUMO EDUCATIVO
print("\n" + "="*60)
print("RESUMO: COMO USAR OPERAÇÕES VETORIAIS")
print("="*60)

print("""
1. ESTRUTURA BÁSICA:
   modelo.wv.most_similar(
       positive=['palavra1', 'palavra2'],  # O QUE VOCÊ QUER
       negative=['palavra3'],               # O QUE VOCÊ NÃO QUER
       topn=5                               # QUANTOS RESULTADOS
   )

2. EXEMPLOS PRÁTICOS:
   
   a) Similaridade simples:
      • positive=['python']
      → Qual palavra é similiar a python?
      
   b) Combinação:
      • positive=['python', 'web']
      → Qual palavra fica perto de python AND web?
      
   c) Subtração:
      • positive=['desenvolvedor'], negative=['programador']
      → Qual é DESENVOLVEDOR mas NÃO programador?
      → (características únicas de desenvolvedor)
      
   d) Analogias:
      • positive=['python', 'rápido'], negative=['lento']
      → Python + Rápido - Lento = ?
      → (Python em contexto de velocidade)

3. INTERPRETAÇÃO DOS RESULTADOS:
   
   Score 0.95 = MUITO similiar (praticamente sinônimo)
   Score 0.70 = Relacionado (mesmo contexto)
   Score 0.50 = Pouco relacionado
   Score 0.30 = Quase sem relação
   Score 0.10 = Não relacionado

4. DICAS PARA BONS RESULTADOS:
   
   ✓ Use palavras que existem no modelo
   ✓ Use palavras relacionadas no positive
   ✓ Use negative com moderação
   ✓ Phrases longas funcionam melhor com corpus grande
   ✓ Tente múltiplas combinações

5. CASOS DE USO REAIS:
   
   • Busca de sinônimos
   • Sistema de recomendação
   • Detecção de spam
   • Análise de sentimentos
   • Tradução automática
   • Chatbots
""")

# TESTE INTERATIVO
print("\n" + "="*60)
print("TESTE FINAL: OPERAÇÕES QUE FUNCIONAM MELHOR")
print("="*60)

# Operações que devem funcionar bem com o corpus grande
operacoes_finais = [
    (['python', 'linguagem'], [], "Python é uma linguagem"),
    (['código', 'programa'], [], "Código e Programa"),
    (['desenvolvedor', 'programador'], [], "Desenvolvedor e Programador"),
    (['dados', 'armazenar'], [], "Dados para armazenar"),
]

for pos, neg, desc in operacoes_finais:
    testar_operacao(pos, neg, desc)




# ------------------------
# 7️⃣ Visualização 2D
# ------------------------
palavras = list(modelo.wv.index_to_key)
vetores = [modelo.wv[w] for w in palavras]

pca = PCA(n_components=2)
resultado = pca.fit_transform(vetores)

plt.figure(figsize=(8,6))
plt.scatter(resultado[:,0], resultado[:,1])

for i, palavra in enumerate(palavras):
    plt.annotate(palavra, xy=(resultado[i,0], resultado[i,1]))

plt.title("Visualização Word2Vec em 2D (PCA)")
plt.show()