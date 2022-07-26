def get_formatted_name(first_name='',last_name='',idade=''):
    pessoa = {}
    full_name = first_name + " " + last_name
    if first_name== "" and last_name=="":
        volta = 0
        while volta!=1:
            first_name = input("Primeiro nome")
            pessoa['primeiro nome'] = first_name
            last_name= input("Ultimo nome")
            pessoa['ultimo nome'] = last_name
            idade = input('Idade')
            if idade.isnumeric() == True:
                idade = int(idade)
                pessoa['idade']=idade
            full_name = first_name + " " + last_name
            volta += 1
    return pessoa





Arrumado = get_formatted_name()
print(Arrumado)