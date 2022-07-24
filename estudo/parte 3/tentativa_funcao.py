produto = {}
produtos = []
def cadastrar(nome,preco,codigo,departamento):
    produto.clear()
    if len(nome)>=1:
        produto['nome']: f'{nome}'

    if preco>=1:
        produto['preco']= f'{preco}'

    if codigo >= 4 :
        produto['codigo'] = f'{codigo}'

    if len(departamento)>=1:
        produto['departamento']= f'{departamento}'

    print(produto)
    produtos.append(produto.copy())
    #NAO ESQUECER DE FAZER UMA COPIA DO DICIONARIO PRODUTO,SE NAO ELE VAI SER SEMPRE DELETADO PELO ULTIMO QUE FOR
    #CADASTRADO

def titulo(mensagem):
    tamanho = len(mensagem)+2
    print("-"*tamanho)
    print(f' {mensagem}')
    print("-"*tamanho)

titulo("Tabela de valores")
while True:
    cadastro = input('Deseja cadastrar um produto? [S] ou [N]').upper()
    while cadastro!= "S" and cadastro!='N':
        cadastro = input('Deseja cadastrar um produto novo?[S] ou [N]').upper()
    if cadastro == "S":
        NOME = str(input("Informe o nome do produto:"))
        while len(NOME) == 0 :
            NOME = str(input("NOME:"))

        PRECO = float(input('Informe o preço do produto:'))
        while PRECO <=0:
            PRECO = float(input("PREÇO:"))

        CODIGO = int(input("Informe o código do produto:"))
        while CODIGO < 3 :
            CODIGO = int(input("CÓDIGO:"))

        DEPARTAMENTO = input("Insira o departamento do produto:")
        while len(DEPARTAMENTO) == 0 :
            DEPARTAMENTO = input('DEPARTAMENTO:')

        cadastrar(NOME,PRECO,CODIGO,DEPARTAMENTO)

    if cadastro == "N":
        print('PRODUTOS CADASTRADOS ')
        for num,item in enumerate(produtos):
            print(f'{num}  {item}')