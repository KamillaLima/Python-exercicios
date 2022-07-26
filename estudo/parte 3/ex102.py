# def fatorial(numero,show = False):
#     total = 1
#     while numero!=0:
#         total *= numero
#         numero-=1
#         if mostrar==True:
#             return print(f'{total}' , end=" ")
#
#     if mostrar == False:
#         return print(f"O fatorial de {numero} é {total}")
#
#
# numero = int(input("Informe um valor paraver seu fatorial:"))
# mostrar = int(input("Deseja ver apenas o resultado[1] ou o passo a passo[2]? "))
# if mostrar== 1:
#     mostrar=False
# if mostrar ==2:
#     mostrar=True
#
# print(fatorial(numero, show=False))

def fatorial(dado,show =False):
    valor = 1
    if show==False:
        while dado!=0:
            valor*=dado
            dado-=1
        return print(valor)
    else:
        while dado > 0:
             valor *= dado
             print(f' {dado} x',end="")
             dado -= 1
        print(f'= {valor}')

fatorial(5,show=True)