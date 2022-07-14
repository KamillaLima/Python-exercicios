soma = 0
contagem = 0
while True:
    numero = int(input('Digite um valor'))
    if numero==999:
        break

    else:
        soma += numero
        contagem += 1
print(f"A soma de {contagem} valores resultou em {soma}")
