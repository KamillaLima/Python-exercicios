# def ler(valor=0):
#     if valor==0:
#         print("Voce nao digitou nenhum valor")
#     else:
#         return valor
#
#
# numero = str(input("Informe um número:"))
# if numero == "":
#     numero=0
#     ler(numero)
# else:
#     numero = int(numero)
#     print(f'Voce digitou o número {ler(numero)}')
#
#


# def leiaint(txt):
#      while True:
#           print('-' *45)
#           n = str(input(txt))
#           if n.isnumeric():
#                print(f'Você acabou de digitar o número {n}')
#                break
#           else:
#                print('ERRO! Digite um número inteiro válido.')
#
#
# #Programa principal
# n = leiaint('Digite um número aqui:')


def subtrair(mensagem):
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            return n
        else:
            print("ERRO")


n =print(subtrair('Valor'))