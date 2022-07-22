# informacoes = {'nome': str(input("Informe o seu nome : ")),'media': float(input('Informe sua média : '))}
# for k,v in informacoes.items():
#     print(f'{k} : {v}')
# if informacoes['media']> 7:
#         print('voce foi aprovado!')
# else:
#         print('voce foi reprovado!')
#
volta=0
informacoes = dict()
informacoes['nome'] = str(input('Informe o seu nome: '))
informacoes['media'] = float(input('Informe a sua média: '))
for k,v in informacoes.items():
    if volta == 0:
        print(f'O seu {k} é {v}! ')
    else:
        print(f'A sua {k} é de {v}')
    volta+=1

if informacoes['media']<5:
    print('voce está de reprovado')
elif informacoes['media'] >=5 and informacoes['media'] <=6.9:
    print('Voce está de recuperação')
else:
    print('Você foi aprovado!!')