nome = input("Informe o seu nome completo").strip()
print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(len(nome) - nome.count(' '))
separa = nome.split()
#aqui ta pegando a quant de caracteres no nome e dps ta subtraindo a quantidade de espaços através do count ' '
print(f"a quantidade de caracteres no primeiro nome é e a palavra é {separa[0]}")