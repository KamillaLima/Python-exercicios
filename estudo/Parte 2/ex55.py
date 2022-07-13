maior = 0
menor =0
for c in range(1,5+1,1):
    peso = float(input(f"Informe o peso da {c}º pessoa:"))
    if c==1:
        c = maior
        c = menor
    else:
       if maior<peso:
           peso=maior

       if peso<maior:
           peso=menor

print(f"O maior peso entre os citados foi {maior}KG e o menor peso entre os citados foi {menor}KG")


