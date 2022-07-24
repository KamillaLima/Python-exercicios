from time import sleep
def contagem (i,f,p):
    """
    para criar esse param de uma vez,é só digitar 3 aspas duplas e para visualizar essas informações é só fazer
    help(nome da função) - help(contagem)
    :param i: recebe o valor de inicio
    :param f: recebe o valor para finalizar
    :param p: recebe o valor que irá pular
    :return:
    """
    print(f"{'Contagem':^40}")
    if i<=f:
        if p>0:
            for cont in range(i,f+1,p):
                sleep(0.3)
                print(cont, end=" ")
        if p<0:
            p *= -1
            #transformando o p negativo em positivo
            for cont in range(i,f+1,p):
                sleep(0.3)
                print(cont,end=" ")
    if i >=f:
        if p>0:
            p *= +1
            for cont in range(i,f-1, p):
                sleep(0.3)
                print(cont, end=" ")
        if p<0:
            for cont in range(i,f-1, p):
                sleep(0.3)
                print(cont, end=" ")
    print("FIM!")

contagem(int(input("Digite o número de inicio: ")),(int(input("Digite o valor final: "))),(int(input("Digite o passo: "))))