volta = 0
lista = []
continuar = "S"
while continuar == "S":
    valor = int(input("Digite um valor: "))
    if volta == 0:
        lista.append(valor)
    else:
        if valor in lista:
            print("Valor repetido")

        else:
            lista.append(valor)

    continuar = input("Deseja continuar? [S] ou [N]").upper()
    volta+=1

print(lista)



