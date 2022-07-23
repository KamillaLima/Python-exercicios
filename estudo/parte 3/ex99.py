#SEM USAR LISTAS

# def descobrir(*valores):
#     tamanho = len(valores)
#     maior = max(valores)
#     menor = min(valores)
#     print(f'Foram digitados {tamanho} números,o maior entre eles é {maior} e o menor entre eles é {menor}')
#
#
# descobrir(1, 454, 3, 2, 2, -98, 45, 5)





#USANDO LISTAS



def descobrir(lst):
    tamanho = len(lst)
    maior = max(lst)
    menor = min(lst)
    print(f'Foram digitados {tamanho} números,o maior entre eles é {maior} e o menor entre eles é {menor}')


lista = []
while True:
    valor = int(input("Digite um valor:"))
    lista.append(valor)
    continuar = input("Deseja digitar outro valor? [S] ou [N]").upper()
    if continuar == "N":
        descobrir(lista)
        break