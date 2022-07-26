def avaliar(nota_um,nota_dois,nota_tres):
    avaliacao = {}
    notas = []
    avaliacao['nota UM ']=nota_um
    avaliacao['nota DOIS']=nota_dois
    avaliacao['mota TRES']=nota_tres
    notas.append(nota_um)
    notas.append(nota_dois)
    notas.append(nota_tres)
    maior = max(notas)
    menor = min(notas)
    avaliacao['Maior nota']= maior
    avaliacao['Menor nota']=menor
    media = (nota_um + nota_dois + nota_tres)/3
    avaliacao['Média']=media
    if media < 6:
        avaliacao["Situação"]="REPROVADO"

    else:
        avaliacao['Situação']= "APROVADO"


    return avaliacao

turma = avaliar(10,8,7)
print(turma)