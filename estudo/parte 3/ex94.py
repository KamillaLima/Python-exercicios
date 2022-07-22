continuar = "S"
cadastros = {}
galera = []
mediaIdade = 0
totalCadastro = 0
while continuar == "S":
    cadastros.clear()
    cadastros ['nome'] = input('Informe seu nome : ')
    cadastros ['idade'] = int(input('Informe sua idade : '))
    while cadastros['idade'] <0 and  cadastros['idade'] > 100:
        cadastros['idade'] = int(input('Informe sua idade novamente:'))
    cadastros['sexo'] = input("Informe seu sexo [F] ou [M] : ")
    while cadastros['sexo'] !="M" and cadastros['sexo'] != "F":
        cadastros['sexo'] = input("Informe seu sexo [F] ou [M] : ")
    continuar = str(input("Deseja cadastrar outra pessoa? [S] ou [N] " )).upper()
    while continuar!="S" and continuar!="N":
        continuar = str(input("Deseja cadastrar outra pessoa? [S] ou [N] ")).upper()

    galera.append(cadastros.copy())
    mediaIdade += cadastros['idade']
    totalCadastro+=1

mediaIdade /= totalCadastro
print(galera)
print()
print(mediaIdade)
print()
print(totalCadastro)
for pessoa in galera:
    if pessoa['sexo'] == "F":
        print(f'{pessoa["nome"]} - {pessoa["idade"]}')


print()
for pessoa in galera:
    if pessoa['idade'] > mediaIdade:
        print(f'{pessoa["nome"]} - {pessoa["idade"]} - {pessoa["sexo"]}')



