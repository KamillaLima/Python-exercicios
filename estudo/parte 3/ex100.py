from random import randint
valores = []
def sorteia(lista):
    while len(lista) <5:
        valor = randint(0,9)
        lista.append(valor)
    print(f'Os valores sorteados foram {lista}')


def calcularPar(lista):
    soma=0
    for itens in range (0,len(lista)):
        if lista[itens] %2 == 0:
            soma = soma + lista[itens]

    print(f'Somando os valores pares de {valores} o resultado é de {soma}')

sorteia(valores)
calcularPar(valores)
