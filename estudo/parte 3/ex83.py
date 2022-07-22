pilha = []
expressao = input("Informe sua expressão")

#varrer a expressão
for parenteses in expressao:
    if parenteses == "(":
        pilha.append("(")

    elif parenteses == ")":
        #caso já tenha um ( dentro da pilha,ele será apagado,como se tivesse fechado os ()
        if len(pilha)>0:
            pilha.pop()

        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print("Expressão válida")
else:
    print("Expressão inválida")