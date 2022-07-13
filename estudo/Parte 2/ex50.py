s = 0
for contagem in range(0,7,1):
    valor = int(input("Digite o valor"))
    if valor %2==0:
        s +=valor
print(f"A soma dos valores é {s}")