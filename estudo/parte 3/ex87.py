fileiraZero = []
fileiraUm = []
fileiraDois = []
total = []
pares = coluna = x = y = volta = maior =  0
while volta <9:
    valor = int(input(f'Insira um valor para {x},{y} : '))
    if len(fileiraZero) <= 2:
        fileiraZero.append(valor)

    elif len(fileiraUm) <=2:
        fileiraUm.append(valor)

    elif len(fileiraDois) <=2:
        fileiraDois.append(valor)

    volta+=1
    y+=1
    if volta==3 or volta==6 or volta==9:
        x+=1
        y=0

for N in range(0,len(fileiraZero)):
    print(f'[{fileiraZero[N]}]', end="")
print()
for N in range(0,len(fileiraUm)):
    print(f'[{fileiraUm[N]}]', end="")
print()
for N in range(0,len(fileiraDois)):
    print(f'[{fileiraDois[N]}]',end="")

print()
total.extend(fileiraZero)
total.extend(fileiraUm)
total.extend(fileiraDois)
for n in range(0,len(total)):
    if n % 2 ==0:
        pares+=n
print(f'A soma dos números pares presentes nessa matriz é de: {pares}')
soma= []
soma.append(fileiraZero[0])
soma.append(fileiraUm[0])
soma.append(fileiraDois[0])
for s in range (0,len(soma)):
    coluna += soma[s]

print(f'A soma dos números presentes na terceira coluna é {coluna}')
for i in range(0,len(fileiraUm)):
    if i == fileiraUm[0]:
        maior = fileiraUm[i]

    else:
        if maior < fileiraUm[i] :
            maior = fileiraUm[i]

print(f'O maior valor da segunda fileira é {maior}')