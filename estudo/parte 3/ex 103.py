def informacoes(nome="<desconhecido> ",gols= 0 ):
    return print(f'O jogador {nome} fez {gols} gols')


nome = str(input("Informe o seu nome")).strip()
if nome == "":
    nome="<desconhecido>"

gols = str(input("Quantidade de gols"))
if gols == "":
    gols = 0
else:
    gols = int(gols)

informacoes(nome,gols)