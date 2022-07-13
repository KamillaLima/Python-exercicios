# num = input("Informe um valor")
# print(" ".join(num))
#
# cidade = input("Informe o nome de uma cidade").upper()
# city = cidade.split()
# if city[0] == 'SANTO':
#     print('A primeira palavra é Santo')
# else:
#     print(' A primeira palavra NÃO é Santo')
#

# nome = input('Informe o seu nome completo').upper()
# print(nome)
# if 'SILVA' in nome:
#      print('Voce possui Silva em seu nome')
# else:
#     print('voce nao possui silva em seu nome')

# nome = input('Informe seu nome completo:').strip().title()
# Nome = nome.split()
# print(f'O seu primeiro nome é {Nome[0]} e o seu último nome é {Nome[-1]}')

nome = input('Informe o seu nome completo:').strip().title()
print(f'O seu nome contêm {nome.count("a")} letra(s) A !')
print(nome.find('a'))
print(nome.rfind('a'))