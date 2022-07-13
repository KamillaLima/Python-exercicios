num1 = float(input("Informe o primeiro valor:"))
num2 = float(input("Informe o segundo valor:"))
maior = num1
if maior < num2:
    maior = num2

menor = num2
if menor > num2:
    menor = num2
continuar = "S"
while continuar == "S" :
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Dividir')
    print('[4] Maior')
    print('[5] Sair')
    opcao= int(input("Qual opção voce deseja realizar?"))
    if opcao ==1:
        print(f"A soma será de {num1} + {num2} = {num1+num2}")

    elif opcao==2:
        print(f"A multiplicação será de {num1} X {num2} = {num1 * num2}")

    elif opcao ==3:

        print(f"A divisão entre {maior} / {menor} = {maior/menor}")

    elif opcao == 4:
        print(f"O maior valor é {maior}")

    elif opcao== 5:
        continuar = "N"

    else:
        print("Digite uma opção válida")
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Dividir')
        print('[4] Maior')
        print('[5] Sair')
        opcao = int(input("Qual opção você deseja realizar?"))


print("Volte sempre!")