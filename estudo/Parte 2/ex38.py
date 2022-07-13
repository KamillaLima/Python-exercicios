num = float(input("\033[0;34mInforme o primeiro número\033[m"))
num2 = float(input(" \033[0;31mInforme o segundo número\033[m"))
if num > num2:
    print(f"O número \033[0;34m{num}\033[m é maior que o número \033[0;31m{num2}\033[m")
elif num == num2:
    print(f"O número \033[0;31m{num2}\033[m é igual ao número \033[0;34m{num}\033[m")
else:
    print(f"O número \033[0;31m{num2}\033[m é maior que o número \033[0;34m{num}\033[m")