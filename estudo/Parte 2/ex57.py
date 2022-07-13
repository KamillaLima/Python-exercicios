sexo = input("Informe o seu sexo utilizando [M] ou [F]").strip().upper()
print(sexo)
while sexo != "M" and sexo!= "F":
    sexo = input("Dado inválido,informe novamente:").strip().upper()
print("Vamos prosseguir com o seu cadastro!")