numero = 0
lista = 0
contagem = 0
while numero != 999:
    numero = int(input("Informe um valor: [digite 999 para sair]"))
    if numero != 999:
        lista += numero
        contagem += 1

print(f"A soma dos {contagem} valor(es) foi de {lista}")

