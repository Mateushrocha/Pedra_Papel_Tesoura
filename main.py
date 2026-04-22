import random

def funcaoJogadaBot(adversario):
    jogada =  random.randint(1, 3)
    if jogada == 1:
        adversario = 1
    elif jogada == 2:
        adversario = 2
    elif jogada == 3:
        adversario = 3
    return adversario

def categorizar(a):
    if a == 1:
        return "🪨"
    elif a == 2:
        return "📄"
    elif a == 3:
        return "✂️"

while True:
    adversario = None
    print("1 - Pedra 🪨")
    print("2 - Papel 📄")
    print("3 - Tesoura ✂️")
    jogadaPlayer = input("Qual será sua jogada? Digite o apenas index")

    try: jogadaPlayer = int(jogadaPlayer)
    except: 
        print("DIGITE UM VALOR VALIDO")
        continue

    if jogadaPlayer not in [1, 2, 3]:
        print("DIGITE APENAS O INDEX DO VALOR DESEJADO")
        continue 

    jogadaBot = funcaoJogadaBot(adversario)

    if jogadaPlayer == jogadaBot:
        print("EMPATE")
    elif jogadaPlayer == 1 and jogadaBot == 2:
        print("perdeu 🥺")
    elif jogadaPlayer == 1 and jogadaBot == 3:
        print("Venceu 🥇🏆")
    elif jogadaPlayer == 2 and jogadaBot == 1:
        print("perdeu 🥺")
    elif jogadaPlayer == 2 and jogadaBot == 3:
        print("Venceu 🥇🏆")
    elif jogadaPlayer == 3 and jogadaBot == 2:
        print("Venceu 🥇🏆")
    elif jogadaPlayer == 3 and jogadaBot == 1:
        print("perdeu 🥺")
    print(f"Seu adversario jogou {categorizar(jogadaBot)}")
