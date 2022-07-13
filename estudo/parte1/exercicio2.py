import math
import random
ca = float(input('Informe o valor do cateto adjacente'))
co = float(input('Informe o valor do cateto oposto'))
hi = math.hypot(ca , co)
print(f'O valor da hipotenusa é de {hi:.2f}')

ang = float(input("Informe o valor do ângulo:"))
co = math.cos(math.radians(ang))
#pego o ang,converto para radiano e depois calculo o cosseno
se = math.sin(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O seno desse angulo é {se:.2f}, o cosseno desse angulo é {co:.2f} e a tangente é {tg:.2f}')


n1 = input('Nome do primeiro aluno')
n2 = input('Nome do segundo aluno')
n3 = input('Nome do terceiro aluno')
n4 = input('Nome do quarto aluno')
lista = [n1,n2,n3,n4]
sorteio = random.choice(lista)
print(f'O sorteado foi {sorteio}')
#sorteia um dos elementos da lista


valor = input('informe o primeiro nome')
valor2 = input('informe o segundo nome')
total = [valor,valor2]
random.shuffle(total)
print(f'{total}')
#embaralha os elementos dentro da lista
#se valor= kamilla e valor2=edi,usando o shuffle o valor=edi e valor2=kamilla