continuar = "S"
soma = volta = maior = menor = 0
while continuar == "S":
    numero = int(input("Digite um valor"))
    soma+=numero
    volta+=1
    if volta ==1:
        maior = numero
        menor = numero
    elif volta>1:
        if maior<numero:
            maior = numero

        elif menor>numero:
            menor = numero
    continuar = input("Deseja continuar?").upper()

print(f'A soma de {volta} valores é de {soma} e a média é de {soma/volta}')
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")