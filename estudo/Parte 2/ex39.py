from datetime import date
atual = date.today().year
nascimento = int(input("Informe o ano de nascimento:"))
calc = atual - nascimento
if calc==18:
    print("Você deve se alistar esse ano!")

elif calc < 18:
    print("Você ainda não necessita se alistar")

elif calc > 18:
    atraso = calc-18
    print("Você já deveria ter se alistado!")
    print(f"Você está atrasado há {atraso} anos")
    print(f"Você deveria ter se alistado em {atual-atraso}")
