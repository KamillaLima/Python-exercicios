import random
num1 = random.randint(0,10)
num2 = random.randint(0,10)
num3 = random.randint(0,10)
num4 = random.randint(0,10)
num5 = random.randint(0,10)
conjunto = (num1,num2,num3,num4,num5)
print(conjunto)
print(f'o valor máximo entre os números do conjunto é {max(conjunto)}')
print(f'O valor mínimo entre os números do conjunto é {min(conjunto)}')