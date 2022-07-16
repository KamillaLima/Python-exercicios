print(f'{"Listagem de preços":-^50}')
listagem = ('creme',10.50,'escova',23.50,'tinta',26.87)
for item in range(0,len(listagem)):
    if item % 2 ==0:
        print(f'{listagem[item]:.<20}' , end=" ")
        #                              , end= " " vai fazer com que o próximo print de valor fique ao lado do nome do produto

    else:
        print(f'R${listagem[item]:>7.2f}')