from time import sleep
nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota:"))
media = (nota1 + nota2)/2
print('Calculando...')
sleep(3)
if media >= 7.0:
    print("PARABÉNS!")
elif media>=5.1 and media <=6.9:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")