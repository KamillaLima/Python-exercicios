print("Irei te auxiliar na compra de sua residência !")
valor = float(input("Informe o valor da residência : R$"))
salario = float(input("Informe o seu salário mensal : R$"))
anos = int(input("Em quantos anos você deseja financiar a sua residência?"))
meses = anos *12
print()
print(f"Voce pagará a casa por {meses} meses.")
prestacao = valor/meses
print(f"A prestação será de R${prestacao:.2f} por mês.")
valMaximo = (salario*3)/10
print()
if prestacao > valMaximo :
    print('\033[0;30;41mInfelizmente o seu financiamento não foi aprovado\033[m')
else:
   print('\033[0;30;42mParabéns!O seu financiamento foi aprovado!\033[m')

