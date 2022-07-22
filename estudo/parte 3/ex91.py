import random
from operator import itemgetter
jogadores = {'jogador1' : random.randint(1,6),'jogador2':random.randint(1,6),'jogador3' :random.randint(1,6),'jogador4':random.randint(1,6)}
for k,v in jogadores.items():
    print(f'{k} tirou {v}')

#aqui eu to criando uma lista chamada ordenado,ela vai ir do maior para o menor(atraves do sorted e reverse=true),quero
#usar os dados do jogadores.items(),key=itemgetter(1)ele vai pegar o valor(por causa do 1) ao invés da chave(que seria o 0)
ordenado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ordenado)
for i,v in enumerate(ordenado):
    print(f'{i} lugar , {v[0]} com {v[1]} pontos')