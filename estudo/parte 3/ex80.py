volta = 0
lista = []

while volta <= 2 :
    num = int(input((f"Digite o {volta}° valor:")))
    if volta==0:
        lista.append(num)
        print(f"Adicionado na posição {volta} da lista")
    else:
        if num in lista:
            print("Valor duplicado")
        elif volta == 1 :
                if num > lista[0]:
                    print(f'Valor adicionado na posição 1')
                    lista.insert(1,num)
                else:
                    print(f'valor adicionado na posição 0 ')
                    lista.insert(0,num)

        elif volta ==2 :
                    if num > lista[0] and num>lista[1]:
                        print(f'Valor adicionado na posição 2')
                        lista.insert(2,num)
                    elif num>lista[0] and num<lista[1]:
                            print(f'valor adicionado na posição 1 ')
                            lista.insert(1,num)
                    else:
                        print(f'valor adicionado na posição 0 ')
                        lista.insert(0,num)
        elif volta==3:
            if num >lista[0] and num>lista[1] and num>lista[2]:
                print(f'Valor adicionado na posição 3')
                lista.insert(3,num)
            elif num>lista[0] and num<lista[1]


    volta+=1
print(lista)