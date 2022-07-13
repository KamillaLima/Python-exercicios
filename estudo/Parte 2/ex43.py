from time import sleep
print("CALCULANDO IMC")
altura = float(input("Informe sua altura "))
peso = float(input("Informe o seu peso "))
imc = peso / (altura*altura)
print("CALCULANDO...")
sleep(3)
print(f"O seu imc é de {imc:.2f}")
if imc < 18.5:
    print("\033[0;31mABAIXO DO PESO")
    print(" \033[0;31mPROCURE UM ESPECIALISTA URGENTE!")

elif imc >= 18.5 and imc<25:
    print("\033[0;32mPESO IDEAL")

elif imc>=25 and imc <30:
    print("\033[0;33mSOBREPESO")
    print("\033[0;33mPROCURE UM ESPECIALISTA")

elif imc>=30 and imc<40:
    print("\033[0;33mOBESIDADE")
    print("\033[0;33mPROCURE UM ESPECIALISTA")
else:
    print("\033[0;31mOBESIDADE MÓRBIDA")
    print(" \033[0;31mPROCURE UM ESPECIALISTA URGENTE!")
