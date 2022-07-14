MulherIdade = 0
continuar = "S"
voltaIdade = 0
homem = 0
while continuar == "S":
    idade = int(input("IDADE:"))
    sexo = input("SEXO [M] OU [F]:").upper().strip()
    continuar = input("Deseja continuar ? [S] ou [N]").upper().strip()
    if idade>=18:
        voltaIdade+=1

    elif sexo == "F":
        if idade<20:
            MulherIdade+=1

    if sexo == "M":
        homem+=1

    elif continuar =="N":
        break

print()
print(f"Total de pessoas com mais de 18 anos: {voltaIdade}")
print(f"Total de homens cadastrados: {homem}")
print(f"Total de mulheres com menos de 18 anos: {MulherIdade}")