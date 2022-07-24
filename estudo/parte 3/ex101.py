from datetime import date
hoje = date.today().year
def calcularIdade(nascimento):
    idade = hoje - nascimento
    print(f"A sua idade atual é de {idade} é o direito a votação é: ",end="")
    if idade <= 15:
        print("NEGADO")
    elif idade>= 16 and idade<=17 or idade>=70:
        print("OPCIONAL")
    elif idade>=18 or idade <=69:
        print('OBRIGATÓRIO')

nascimento = int(input("Informe a sua data de nascimento"))
while len(str(nascimento)) < 4 or nascimento>hoje:
    nascimento = int(input("Informe uma data de nascimento válida"))
calcularIdade(nascimento)



#USANDO RETURN _____________________________________________________________________________________________________

from datetime import date
from time import sleep
hoje = date.today().year
def calcularIdade(nascimento):
    idade = hoje - nascimento
    sleep(0.5)
    print (f"A sua idade atual é de {idade} é o direito a votação é: ",end="")
    if idade <= 15:
        return ("NEGADO")
    elif idade>= 16 and idade<=17 or idade>=70:
        return ("OPCIONAL")
    elif idade>=18 or idade <=69:
        return ('OBRIGATÓRIO')

nascimento = int(input("Informe a sua data de nascimento"))
while len(str(nascimento)) < 4 or nascimento>hoje:
    nascimento = int(input("Informe uma data de nascimento válida"))

print(calcularIdade(nascimento))


