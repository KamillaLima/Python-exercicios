def calcular(a,b):
    area = a *b
    print(f"A area de {a} x {b} é de {area} metros quadrados")


# print('--------Calculando área--------')
# comprimento = float(input("Informe o comprimento do terreno em metros:"))
# largura = float(input("Informe a largura do terreno em metros:"))
# calcular(comprimento,largura)
#caso a ordem de a e b importem na função eu posso fazer da seguinte maneira:
#calcular(a=comprimento,b=largura)


print('--------Calculando área--------')
calcular(float(input("Informe o comprimento do terreno em metros:")),float(input("Informe a largura do terreno em metros:")))