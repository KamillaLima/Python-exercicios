i = int(input("Em qual número a contagem deve se iniciar?"))
f = int(input("Em qual número a contagem deve se encerrar?"))
p = int(input("A contagem deve pular de quanto em quanto?"))

for c in range(i,f+1,p):
    print(c)

print("FIM DA CONTAGEM")