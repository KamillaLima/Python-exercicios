# valores = ["kamilla",'lima','abce']
# valores.sort()
# print(valores)
# for c,v in enumerate(valores):
#     print(f'Na posição {c} encontrei o número {v}')
valores = []
volta = 0
while volta <=4:
    numero= int(input(f"Informe um valor para a posição {volta}"))
    valores.append(numero)
    volta+=1

print(valores)
#Dessa forma retira os [] quando for printar
print()
maior = max(valores)
menor = min(valores)
vezesMaior = []
vezesMenor = []
for p in range(0,len(valores)):
    if valores[p]==maior:
        vezesMaior.append(p)
    elif valores[p]==menor:
        vezesMenor.append(p)

print(f'O maior valor digitado foi {maior} e ele foi encontrado nas posições: ' , end=" ")
print(*vezesMaior, sep=', ')
print(f'\nO menor valor digitado foi {menor} e ele foi encontrado nas posições: ', end=' ')
print(*vezesMenor, sep =", ")