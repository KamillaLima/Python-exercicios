contador = 0
soma = 0
for c in range(1,500+1,1):
    if c % 2 !=0:
        if c%3==0:
            soma+=c
            contador+=1

print(f"A soma dos {contador} valores,resultou no valor {soma}")