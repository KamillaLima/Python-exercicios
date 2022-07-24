def somar(a,b,c=0):
    #o C esta valendo zero,pois caso a pessoa nao escreva 3 valores,a função ainda assim irá funcionar,já que nao
    #necessita obrigatoriamente de 3 parametros

    #Posso colocar A,B e C valendo zero,pois também da certo,já que vai se tornar opcional que o usuário digite
    #um,dois ou tres valores

    #As variaveis que são criadas dentro de uma função,não conseguem ser chamadas fora da função,exemplo a var soma :
    soma = a+b+c
    print(f"A soma de {a}+ {b} + {c} = {soma}")
    #A variavel V fora da função tem valor 6,se ela for chamada dentro da função será criada uma nova variavel V
    #apenas para ser utilizada dentro da função,caso eu não queira que isso aconteça,eu preciso escrever dentro da
    #função :
    global V



def subtrair(a,b,c):
    #criei uma variavel chamada sub,e esse return sub ta meio que pegando a var sub e fazendo ela funcionar fora
    #função
    sub = a - b - c
    return sub
    #Posso fazer um return chamando uma variavel,ou True e False,ou um valor


V = 6
somar(1,2)
#  OU
somar(1,2,3)

# print(f"A soma é de {soma}")

r1 = subtrair(10,3,1)
#posso tanto criar uma variavel ou printar diretp
print(subtrair(82,9,31))
r2 = subtrair(99,43,21)
r3 = subtrair(88,44,22)
print(f"A subtração dos valores mencionados teve como resultado {r1} , {r2} , {r3}")