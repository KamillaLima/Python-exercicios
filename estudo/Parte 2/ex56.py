volta = maior = idadeMulher = MED=0
HomemNome = ""

while volta<4:
    print("-----------")
    nome = input("Nome:")
    idade = int(input("IDADE:"))
    sexo = input ("[M] ou [F]:").upper()
    print("-----------")
    MED= MED + idade
    if sexo == "M":
        if volta==1:
            maior = idade
            HomemNome = nome
        else:
            if maior<idade:
                maior = idade
                HomemNome = nome

    elif sexo == "F":
        if idade < 20:
            idadeMulher +=1

    volta += 1



print(f"A média das idades é de {MED/4}")
print(f"O nome mais velho se chama {HomemNome} e tem {maior} anos")
print(f"{idadeMulher} mulher(es) tem menos de 20 anos ")


