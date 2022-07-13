from datetime import date
atual = date.today().year
nascimento = int(input("Informe a sua data de nascimento:"))
idade = atual-nascimento

if idade <= 9:
    print("Você está na categoria INFANTIL")

elif idade >= 10 and idade <=14:
    print("Você está na categoria MIRIM")

elif idade >=15 and idade<=19:
    print("Você está na categoria JÚNIOR")

elif idade>=20 and idade <=25:
    print("Você está na categoria SÊNIOR")

else:
    print("Você está na categoria MASTER")