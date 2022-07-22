# print(f'{"Listagem de preços":-^50}')
# listagem = ('creme',10.50,'escova',23.50,'tinta',26.87)
# for item in range(0,len(listagem)):
#     if item % 2 ==0:
#         print(f'{listagem[item]:.<20}' , end=" ")
#         #                              , end= " " vai fazer com que o próximo print de valor fique ao lado do nome do produto
#
#     else:
#         print(f'R${listagem[item]:>7.2f}')
#


lista =[]
volta = 0
while volta <=2:
    nome = input('Informe o nome do produto:')
    preco = float(input('Informe o valor do produto'))
    lista.append(nome)
    lista.append(preco)
    volta+=1

print(f'{"Listagem de preços":*^40}')
print()
for i in range(0,len(lista)):
    if i %2==0:
        print(f'{lista[i]:.<30}' , end=" ")

    else:
        print(f'R${lista[i]:>7.2f}')