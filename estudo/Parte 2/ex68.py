from random import randint
print("ATENÇÃO : O sorteio só acontece entre 0 a 10 ")
pontos = 0
while True:
    sorteio = randint(0, 10)
    chute = int(input('Digite seu chute!'))
    if chute == sorteio:
        pontos+=1
    else:
        print(f'Você fez {pontos} pontos!')
        print("VOCE PERDEU")
        break