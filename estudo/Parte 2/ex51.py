termoUm = int(input("Informe o primeiro termo"))
razao = int(input("Informe a razão"))
decimo = termoUm + (10-1)*razao
for c in range(termoUm,decimo+razao,razao):
    print(f"{c}")