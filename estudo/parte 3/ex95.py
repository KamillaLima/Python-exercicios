jogadores = {}
golsTotal = 0
golsPartida = []
continuar = "S"
total = []
while continuar == "S":
    jogadores.clear()
    golsPartida.clear()
    golsTotal = 0
    gols = 0

    jogadores ['nome']= str(input('NOME: '))
    partidas = int(input("PARTIDAS JOGADAS: "))

    for jogos in range(0, partidas):
        gols = int(input(f'partida {jogos}: '))
        golsPartida.append(gols)
    golsTotal = sum(golsPartida)


    jogadores['gols'] = golsPartida[:]
    jogadores['total'] = golsTotal
    continuar = input("Gostaria de continuar? [S] ou [N]").upper()


    total.append(jogadores.copy())


print("-"*60)
print(f'{"cod":<2}', end= "     ")
print(f'{"nome":<8}', end="            ")
print(f'{"gols":>8}', end= "           ")
print(f'{"total":>2}')
print("-"*60)

# for cont in range(0,len(total)):
#     print(f'{cont} ... {total[cont]}')
for k,v in enumerate(total):
    print(f'{k :<4}')
    for d in v.values():
        print(f'{str(d):<15}',end= " ")

while True:
        print()
        mostrar =int(input("Deseja mostrar as informações de qual?"))
        if mostrar != 999:
            print(f'LEVANTAMENTO DO JOGADOR------{total[mostrar]["nome"]}')
            for lin in range(0,(len(total[mostrar]['gols']))):
                print(f"Partida {lin} : Gols {total[mostrar]['gols'][lin]}")
        else:
            break
