jogador = {'nome' : str(input('Nome do jogador:')) , 'partidas' : int(input("Qual o total de partidas jogadas?"))  }
partidas = []
total = 0
for jogos in range(0,jogador['partidas']):
    gols = int(input(f'partida {jogos}: '))
    partidas.append(gols)

for valores in range (0,len(partidas)):
    total += partidas[valores]

jogador['gols'] = partidas
jogador['total'] = total
print()
print(jogador)
print()
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print()

print(f'O(A) jogador(a) {jogador["nome"]} jogou {jogador["partidas"]} partida(s)')
print()
for i,v in enumerate(jogador['gols']):
    #o i vai ver quantos espaços tem dentro de gol,já o v vai pegar o valor dentro de cada um deles
    print(f'Na partida {i} foram {v} gols')

print()
print(f'O total de gols em {jogador["partidas"]} partidas foi de {jogador["total"]}')