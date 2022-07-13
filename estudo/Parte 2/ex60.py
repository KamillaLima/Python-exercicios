from math import factorial
numero = int(input("Informe um número"))
#fact = factorial(numero)
#print(fact)

#Duas formas de fazer:

multiplicacao =1
while numero!=1:
    multiplicacao *=numero
    numero-=1

print(multiplicacao)