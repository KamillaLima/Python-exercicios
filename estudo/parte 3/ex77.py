# palavras = ('camisa','calça','meia','tenis','ssdjh')
#
# for p in palavras:
#     print(f'\nA palavra {p} tem' , end=" ")
#     #aqui é pra pegarmos uma só palavra da lista
#
#
#     for letras in p:
#         #para cada letra na palavra P
#         #se letra estiver em 'aeiou'
#         if letras in "aeiou":
#             print(f' {letras}' , end ='')

volta=0
lista= []
while volta <=2:
    palavras = input('Digite uma palavra:')
    volta+=1
    lista.append(palavras)
print(lista)

for p in lista:
    print(f'\n{p} possui ', end="")
    for letras in p:
        if letras in "aeiou":
            print(f"{letras}", end="")