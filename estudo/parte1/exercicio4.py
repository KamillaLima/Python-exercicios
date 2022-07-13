# import random
# print("JOGO DA ADIVINHAÇÃO")
# num1 = int(input("Informe em qual número voce gostaria de iniciar o sorteio"))
# num2 =int(input("Informe em qual número voce gostaria de encerrar o sorteio"))
# num = random.randint(num1,num2)
# valor = int(input("Adivinhe qual número eu pensei?"))
# if valor == num :
#     print("Parabéns!!")
# else:
#     print("Que pena!")
#     print(f"Eu pensei no valor {num}")
#
#

# vel = int(input("Informe a velocidade do carro : Km/h"))
# if vel >=81 :
#     multa = (vel-80)*7
#     print(f"Você foi multado em R${multa}")
# else:
#     print("Dirija com segurança e boa viagem!")
#


# numero = int(input("Informe um valor"))
# if (numero % 2) == 0:
#     print("É um valor PAR")
# else:
#     print('É um valor ÍMPAR')

# km = int(input("Quantos quilometros terá até chegar no destino final?"))
# if km <= 200:
#     preco = km*0.15
#     print(f"Você irá pagar um total de {preco}")
# else:
#     preco = km*0.45
#     print(f"Você irá pagar um valor de {preco}")
#
# val1 = float(input("Informe o primeiro valor:"))
# val2 = float(input("Informe o segundo valor:"))
# val3 = float(input("Informe o terceiro valor:"))
# menor = val1
# if menor > val2:
#     menor = val2
# if menor > val3:
#     menor=val3
# print(f'O menor valor é o {menor}')
# maior = val1
# if maior < val2:
#     maior = val2
# if maior < val3:
#     maior = val3
# print(f'O maior valor é o {maior}')



# salario = int(input("Informe o seu salário"))
# if salario > 1250 :
#     aumento = (salario*110)/100
#     print(f'Com o aumento o seu salário passará a custar {aumento:.2f}')
# else:
#     aumento = (salario*115)/100
#     print(f'Graças ao aumento o seu salário será de {aumento:.2f}')

print('\033[1;31;43mOlá mundo!\033[m')
#esse \033[m dps de mundo faz com que a cor pegue apenas na frase e não na linha inteira
valor = int(input("Informe um valor"))
valor2 = int(input("Infore um segundo valor"))
print(f"O valor \033[7;33;46m{valor}\033[m somado a \033[7;33;46m{valor2}\033[m resulta em \033[4;35;40m{valor + valor2}\033[m")