p1 = int(input("Informe o primeiro termo"))
razao = int(input("Informe a razão"))
n=10
nova = 1
while nova <= n :
    conta = p1 + (nova-1) * razao
    print(conta ,end=' ')
    nova+=1