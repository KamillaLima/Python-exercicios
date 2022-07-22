# senha=[]
# impares = []
# pares = []
# volta=0
# while volta<=7:
#     valor = int(input(f"Informe o {volta}º valor:"))
#     if valor %2==0:
#         pares.append(valor)
#     else:
#         impares.append(valor)
#     volta+=1
#
# pares.sort()
# print(f'Os números pares são : {pares} ' )
# impares.sort()
# print(f'Os números ímpares são : {impares}')
# senha.extend(impares)
# senha.extend(pares)
# print(f'A senha completa é {senha}',end=" ")

#Outra forma de fazer utilizando apenas uma lista é separar a listona senha em outros duas mini listas

senha = [[],[]]
volta = 0
while volta <=6:
    caracter = int(input("Insira um caracter"))
    if caracter %2==0:
        senha[0].append(caracter)
    elif caracter %2!=0:
        senha[1].append(caracter)

    volta +=1

senha.sort(reverse=True)
print(f'Os numeros pares da senha são {senha[0]}')
print(f'Os números ímpares da senha são {senha[1]}')
print(f'A senha completa é {senha}')