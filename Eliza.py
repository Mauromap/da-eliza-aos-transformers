import re
import random

respostas = {
    r"\b(ola|oi|eai|bom dia|boa tarde|boa noite)\b": [
        "Olá, como você está se sentindo hoje?",
        "Oi, pode me contar o que está passando pela sua mente?",
        "Olá, estou aqui para te ouvir."
    ],

    r"me sinto (.*)": [
        "Por que você se sente {}?",
        "O que faz você se sentir {}?",
        "Você costuma se sentir {} com frequência?"
    ],

    r"estou (.*)": [
        "Há quanto tempo você está {}?",
        "Por que você está {}?",
        "O que levou você a estar {}?"
    ],

    r"eu sou (.*)": [
        "Por que você acha que é {}?",
        "Você gosta de ser {}?",
        "Ser {} te incomoda?"
    ],

    r"eu tenho (.*)": [
        "Por que você tem {}?",
        "Isso te preocupa?",
        "Como você lida com isso?"
    ],

    r"eu quero (.*)": [
        "Por que você quer {}?",
        "O que aconteceria se você conseguisse {}?",
        "Esse desejo é importante para você?"
    ],

    r"eu preciso (.*)": [
        "Por que você precisa {}?",
        "Você realmente precisa disso?",
        "O que aconteceria se não tivesse {}?"
    ],

    r"porque (.*)": [
        "Por que você acha que {}?",
        "Essa pergunta é importante para você?",
        "O que você acha que pode ser a resposta?"
    ],

    r"sim": [
        "Entendo, pode me contar mais?",
        "Você parece ter certeza disso.",
        "Por que você acha que sim?"
    ],

    r"nao": [
        "Por que não?",
        "O que te faz pensar assim?",
        "Você tem certeza disso?"
    ],

    r"amigo|amigos": [
        "Me fale mais sobre seus amigos.",
        "Você confia neles?",
        "Seus amigos te ajudam emocionalmente?"
    ],

    r"familia|pai|mae|irmao|irma": [
        "Me fale mais sobre sua família.",
        "Como é sua relação com eles?",
        "Sua família influencia suas emoções?"
    ],

    r"triste|deprimido|mal": [
        "Sinto muito que esteja se sentindo assim.",
        "Quer me contar o que te deixou triste?",
        "Estou aqui para te ouvir."
    ],

    r"feliz|bem|alegre": [
        "Que bom ouvir isso.",
        "O que te deixou feliz?",
        "Você costuma se sentir assim com frequência?"
    ],

    r"ansioso|ansiedade": [
        "O que está causando sua ansiedade?",
        "Você passa por isso com frequência?",
        "Quer falar mais sobre isso?"
    ],

    r"estressado|cansado": [
        "Parece que você está sobrecarregado.",
        "O que está te deixando estressado?",
        "Você tem descansado o suficiente?"
    ],

    r"amor|namorada|namorado|relacionamento": [
        "Relacionamentos podem ser complicados.",
        "Quer me contar mais sobre isso?",
        "Como você se sente nesse relacionamento?"
    ],

    r"trabalho|faculdade|estudo": [
        "Isso parece importante para você.",
        "Está sendo difícil lidar com isso?",
        "Quer falar mais sobre seus estudos ou trabalho?"
    ],

    r"(.*)": [
        "Me conte mais sobre isso.",
        "Como isso faz você se sentir?",
        "Por que você diz isso?",
        "Isso é importante para você?",
        "Interessante, pode explicar melhor?",
        "Continue, estou ouvindo.",
        "Como você reage a isso?",
        "O que você acha disso?",
        "Pode falar mais.",
        "Entendo, e o que mais?"
    ]
}

def main():
    while True:
        mensagem = input("Você:" ).lower()
        if mensagem.lower() == "tchau":
            print("Eliza: Até mais!")
            break
        else:
            print("Eliza: " + match_resposta(mensagem))

def match_resposta(mensagem):
    for pattern, lista in respostas.items():
        if re.search(pattern, mensagem):
            resposta = random.choice(lista)

            match = re.search(pattern, mensagem)
            if match and match.groups():
                try:
                    return resposta.format(*match.groups())
                except:
                    return resposta
            return resposta

    return "Pode me explicar melhor?"

if __name__ == "__main__":
    main()