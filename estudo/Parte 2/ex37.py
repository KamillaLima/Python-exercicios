menu = "SIM"
num = int((input("Informe um número:")))
while menu == "SIM":
    print("Seja bem vindo ao Conversor de bases numéricas")
    print("-------------------------------------------------")
    print()
    print("As opções disponíveis são:")
    print("\033[1;31;43m[1]\033[m Para converter para binário" )
    print("\033[1;32;45m[2]\033[m Para converter para octal")
    print("\033[1;36;44m[3]\033[m Para converter para hexadecimal")
    opcao = int(input("Qual opção você deseja?"))
    if opcao == 1:
        print(f"O número {num} convertido para binário é \033[1;31;43m{bin(num)}\033[m")
        menu = input("Deseja voltar ao menu? digite SIM ou NAO").upper()
    elif opcao == 2:
        print(f"O número {num} convertido para octal é \033[1;32;45m{oct(num)}\033[m")
        menu = input("Deseja voltar ao menu? digite SIM ou NAO").upper()
    elif opcao==3:
        print(f"O número {num} convertido para hexadecimal é \033[1;36;44m{hex(num)}\033[m")
        menu = input("Deseja voltar ao menu? digite SIM ou NAO").upper()

if menu == "NAO":
    print('volte sempre!')
