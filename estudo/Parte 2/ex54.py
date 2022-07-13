from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1,7+1,1):
    nascimento=(int(input(f"Informe a data de nascimento da {c}º pessoa:")))
    idade = atual - nascimento
    if idade <= 17:
        menor+=1
    else:
        maior+=1
print(f"Entre as 7 pessoas,{menor} são menores de idade e {maior} são maiores de idade")