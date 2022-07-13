lado1 = float(input("Informe o primeiro segmento"))
lado2 = float(input("Informe o segundo segmento"))
lado3 = float(input("Informe o terceiro segmento"))

if lado1<lado3+lado2 and lado3<lado1+lado2 and lado2<lado3+lado1:
    print("Será possível formar um triângulo")
    if lado1==lado2 and lado2==lado3 or lado3==lado1 and lado1==lado2:
        print("Será um triângulo EQUILÁTERO")
    elif lado1==lado2 and lado2!=lado3 or lado1==lado2 and lado1!=lado3 :
        print("Será um triângulo ISÓSCELES")
    else:
        print("Séra um triângulo ESCALENO")



else:
    print("Não será possível formar um triângulo")