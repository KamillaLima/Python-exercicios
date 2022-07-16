numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','catorze','quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input(("Qual número você gostaria de ver?")))
while escolha < 0 or escolha >= 21:
    escolha = int(input("Escolha um valor entre 0 a 20"))

print(numeros[escolha])