import random
sorteio = random.randint(0,10)
chute = int(input("Adivinhe qual é o valor que eu pensei:"))
volta=1
print(sorteio)
while (volta<=3):
    if volta >=1 and volta<=2:
        chute = int(input(f"{volta} chance!Tente outra vez:"))
        volta+=1
    else:
            print("ULTIMA CHANCE!")
            chute = int(input(f"Em qual número eu pensei?"))
            volta +=1


if sorteio == chute:
    print("Parabens")

else:
    print("Nao foi dessa vez")
