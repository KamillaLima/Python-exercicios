p1 = int(input("Insira o primeiro termo:"))
r = int(input("Insira a razão"))
termo = 10
volta = 1
mais = 1
while volta<=termo:
    print(p1 + (volta - 1) * r , end=" ")
    volta+=1

while mais!=0:
    mais = int(input("Quer mostrar mais quantos?"))
    soma = (volta+mais)
    while volta!=soma:
        print(p1 + (volta - 1) * r, end=" ")
        volta += 1

print(f"Foram usados {volta-1} termos!")
#subtrair 1 pq a volta se inicia valendo 1
print("Volte sempre")