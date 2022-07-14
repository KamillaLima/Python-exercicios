# while True:
#     numero = int(input("Digite um número e descubra sua tabuada!"))
#     if numero < 0:
#         print("Volte sempre :)")
#         break
#     multiplicador = 0
#     while multiplicador<11:
#         print(f"{numero} x {multiplicador} = {numero*multiplicador}")
#         multiplicador+=1
#
#     if multiplicador==10:
#         numero = int(input("Digite um número e descubra sua tabuada!"))
#         multiplicador = 0
#





numero = int(input("Informe um número:"))
multiplicador = 0
while numero > 0:
    for multiplicador in range(0,11,1):
        print(f"{numero} X {multiplicador} = {numero * multiplicador}")

    if multiplicador <=10:
        numero = int(input("Digite um valor"))

print("Fim do programa!")
