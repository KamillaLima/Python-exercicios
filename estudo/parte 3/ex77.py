palavras = ('camisa','calça','meia','tenis','ssdjh')

for p in palavras:
    print(f'\nA palavra {p} tem' , end=" ")
    #aqui é pra pegarmos uma só palavra da lista


    for letras in p:
        #para cada letra na palavra P
        #se letra estiver em 'aeiou'
        if letras in "aeiou":
            print(f' {letras}' , end ='')
