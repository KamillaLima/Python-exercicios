import random
import emoji
print("PEDRA PAPEL TESOURA")
print()
print("[1]PEDRA")
print("[2]PAPEL")
print("[3]TESOURA")
print()
escolha = int(input("Qual será sua jogada?"))
sorteio = random.randint(1,3)
if escolha == 1:

    if sorteio==1:
        print(emoji.emojize(":robot:ROBO:PEDRA"))
        print(emoji.emojize(":woman:HUMANO:PEDRA"))
        print(emoji.emojize(":oncoming_fist:  X   :oncoming_fist:"))
        print("\033[0;33m-----EMPATE-----")
    elif sorteio == 2:
        print(emoji.emojize(":robot:ROBO:PAPEL"))
        print(emoji.emojize(":woman:HUMANO:PEDRA"))
        print(emoji.emojize(":hand_with_fingers_splayed:  X  :oncoming_fist:  "))
        print("\033[0;31m---PONTO PARA O ROBO---")

    else:
        print(emoji.emojize(":robot:ROBO:TESOURA"))
        print(emoji.emojize(":woman:HUMANO:PEDRA"))
        print(emoji.emojize("  :victory_hand:    X   :oncoming_fist:"))
        print('\033[0;34m---PONTO PARA O HUMANO---')

elif escolha == 2:

    if sorteio ==1:
        print(emoji.emojize(":robot:ROBO:PEDRA"))
        print(emoji.emojize(":woman:HUMANO:PAPEL"))
        print(emoji.emojize(":oncoming_fist:  X :hand_with_fingers_splayed:  "))
        print('\033[0;34m---PONTO PARA O HUMANO---')
    elif sorteio==2:
        print(emoji.emojize(":robot:ROBO:PAPEL"))
        print(emoji.emojize(":woman:HUMANO:PAPEL"))
        print(emoji.emojize(":hand_with_fingers_splayed:  X  :hand_with_fingers_splayed:  "))
        print("\033[0;33m-----EMPATE-----")
    else:
        print(emoji.emojize(':robot:ROBO:TESOURA'))
        print(emoji.emojize(":woman:HUMANO:PAPEL"))
        print(emoji.emojize(" :victory_hand:  X  :hand_with_fingers_splayed:"))
        print("\033[0;31m---PONTO PARA O ROBO---")

elif escolha==3:
    if sorteio==1:
        print(emoji.emojize(":robot:ROBO:PEDRA"))
        print(emoji.emojize(":woman:HUMANO:TESOURA"))
        print(emoji.emojize(":oncoming_fist:  X  :victory_hand: "))
        print("\033[0;31m---PONTO PARA O ROBO---")


    elif sorteio==2:
        print(emoji.emojize(":robot:ROBO:PAPEL"))
        print(emoji.emojize(":woman:HUMANO:TESOURA"))
        print(emoji.emojize(":hand_with_fingers_splayed:  X  :victory_hand:  "))
        print('\033[0;34m---PONTO PARA O HUMANO---')

    else:
        print(emoji.emojize(":robot:ROBO:TESOURA"))
        print(emoji.emojize(":woman:HUMANO:TESOURA"))
        print(emoji.emojize(":victory_hand: X   :victory_hand:"))
        print("\033[0;33m-----EMPATE-----")