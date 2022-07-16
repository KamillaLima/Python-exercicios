times = ("","Palmeiras",'Corinthians','Internacional','Atlético-MG','Fluminense','Atheltico-PR','São Paulo','Santos','Flamengo','Botafogo','Bragantino','Goiás','Cuiabá','Coritiba','América-MG','Avaí','Ceará','Atlético-GO','Juventude','Fortaleza')
for cont in range(1,len(times[:6]),1):
    print(f'Os cinco primeiros colocados são {cont} - {times[cont]}')
print()
print(f'Os últimos colocados são {times[-4:]}')
print()
print(f'Os times em ordem alfabética ficam: {sorted(times)}')
print()
descobrir = int(input('Digite um número e descubra qual time está nessa posição!'))
print(times[descobrir])
print()
print(f'O Palmeiras está na {times.index("Palmeiras")}  posição')

