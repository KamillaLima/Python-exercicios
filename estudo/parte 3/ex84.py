dados = []
total = []
Peso = []
volta = 0
maior = 0
menor = 0
while volta <=2:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    if volta == 0:
        maior = dados[1]
        menor = dados[1]
#Nesse momento,a lista dados estava da seguinte maneira : dados [ 'kamilla' , 58],então quando eu coloco maior= dados[1]
#estou dizendo que o peso da primeira pessoa que se cadastrar será tanto o maior peso quanto o menor
    else:
        if maior < dados[1]:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    volta+=1
# Aqui estou passando as informações da lista dados para a lista total e em seguida limpando a lista dados
    total.append(dados[:])
    dados.clear()

print(f'{volta} pessoas se cadastraram')
print(f"Dessas {volta} pessoas,a(s)com o maior peso são : " , end=" ")
#aqui estou vendo se o peso é igual ao peso maior,caso seja irá exibir o nome da pessoa com esse peso através do p[0]
for p in total:
    if p[1] == maior:
        print(f'{p[0]}')


print(f"E a(s) com o menor peso são : ", end= " ")
for p in total:
    if p[1] == menor:
        print(f'{p[0]}')
