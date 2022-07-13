frase = 'ola mundo'
#vai mostrar quantas letras "o" a palavra possui
print(frase.count('o'))
frase.count('a',0,4)
#vai procurar a letra "a" da posição 0 até a 4
print(frase.find('ndo'))
#vai mostrar em qual posição esse ndo começa,nesse caso o n está na posição 6
print("mundo" in frase)
#vai printar true caso tenha "mundo" na variável frase
print(frase.replace("mundo" , "python"))
#vai trocar a palavra mundo por python na variável frase
print(frase.capitalize())
#só o primeiro caracter da palavra fica em maiusculo

palavra = "      ola"
print(palavra.strip())

#remove os espaços inuteis que forem dados no inicio e no final da frase
print(palavra.rstrip())
#remove apenas os espaçoes do lado direito, fstrip remove apenas os espaços do lado esquerdo

text = 'ola mundo,bem vindo ao python'
print(text.split())
#separa cada uma das palavras em "novas palavras",ou seja,vai parar de considerar o text como uma única str


print("-".join(text))
#entre cada uma das letras será colocado esse "-"
