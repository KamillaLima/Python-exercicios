continuar = 's'
total = maior = menor = volta = 0
NOME = ""
while continuar == 's':
    nome = input('Informe o nome do produto:')
    preco = float(input("Informe o preço do produto:"))
    total += preco
    continuar = input("Deseja continuar?")
    volta += 1
    if volta == 1:
        menor = preco
        NOME = nome

    elif volta > 1:
        if menor > preco:
            menor = preco
            NOME = nome

    elif preco >= 1000:
        maior += 1

    elif continuar == "n":
        break

print("FIM DO PROGRAMA")
print('----------------')
print(f"O total da compra foi de R${total:.2f}")
print(f"O produto mais barato foi um(a) {NOME} no valor de R${menor:.2f}")
if maior >= 1:
    print(f"Temos {maior} produto(s) custando mais de R$1.000,00")

