continuar = "S"
volta =0
lista = []
while continuar == "S":
    numero = int(input("Digite um número:"))
    if volta == 0:
        lista.append(numero)
    else:
        if numero in lista:
            print('NUMERO DUPLICADO')

        else:
            lista.append(numero)
    continuar = input("Deseja continuar? [S] ou [N]:").upper()
    volta+=1
print()
print(f'A lista preenchida fica assim: {lista}')
print(f'Ela possui {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente{lista}')
print()
escolha = int(input("Escolha um valor para descobrir se faz parte da lista:"))
if escolha in lista:
    print(f"O valor {escolha} faz parte da lista")
else:
    print(f'O valor {escolha} NÃO faz parte da lista')