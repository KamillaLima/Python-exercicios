sacar = int(input("Quanto você deseja sacar?"))
valor = 0
cedulaCinq = 0
cedulaDez = 0
cedulaUm = 0

while sacar != 0:
    if sacar >= 50:
        cedulaCinq = sacar // 50
        sacar = sacar-(cedulaCinq*50)


    elif sacar >= 10 and sacar<=49:
            cedulaDez = sacar//10
            sacar = sacar - (cedulaDez*10)

    elif sacar >=1 or sacar<=9:
        cedulaUm = sacar//1
        sacar = sacar - (cedulaUm*1)

print()
print(f"{cedulaCinq} cédula(s) de R$50")
print(f"{cedulaDez} cédula(s) de R$10")
print(f"{cedulaUm} cédula(s) de R$1")
