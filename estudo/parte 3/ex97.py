def escrever(texto):
    tamanho = len(texto)+2
    print("-" *tamanho)
    print(f' {texto}')
    print("-"*tamanho)


escrever(str(input('Digite uma frase : ')))