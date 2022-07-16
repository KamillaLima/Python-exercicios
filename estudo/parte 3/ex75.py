num1 = int(input("Digite um valor:"))
num2 = int(input("Digite o segundo valor"))
num3 = int(input("Digite o terceiro valor"))
num4 = int(input("Digite o quarto valor"))
num5 = int(input("Digite o quinto valor"))
conjunto = (num1,num2,num3,num4,num5)
par = 0
igual = 0
print(conjunto)
print()

#Para descobrir quantas vezes determinado valor apareceu,tem duas formas,uma é usando o count e a outra é fazendo um for
if 9 in conjunto:
    #se o valor 9 estiver presente na tupla,o print abaixo irá ser executado
    print(f'O valor 9 apareceu {conjunto.count(9)} vez(es)')
# for c in range(0,len(conjunto)):
#     if conjunto[c]==conjunto[0]:
#         igual+=1
#
# print(f'O primeiro valor ({conjunto[0]}) aparece {igual} vez(es) na lista')
print()
saber = int(input("Informe qual valor você gostaria de saber a posição que o mesmo se encontra:"))
while saber!=num1 and saber!=num2 and saber!=num3 and saber!=num4 and saber!=num5:
    print(f"Os valores disponíveis são {conjunto}")
    saber = int(input("Informe qual valor você gostaria de saber a posição que o mesmo se encontra"))

print(f'O valor {saber} está na {conjunto.index(saber)+1} posição')
#adicionei um pq ai a posição zero deixa de existir e fica mais fácil pro usuário entender
print()
for cont in range(0,len(conjunto)):
    if conjunto[cont]%2==0:
        par+=1
print(f'O conjunto possui {par} números pares')