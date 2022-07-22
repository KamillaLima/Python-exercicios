from datetime import date
atual = date.today().year
funcionario ={'nome':str(input('Nome:')),'Ano de nascimento':int(input("Ano de nascimento:")),\
              'Carteira de trabalho':int(input('Carteira de trabalho(0 se não tiver)'))}
if funcionario['Carteira de trabalho'] >= 1:
    funcionario ['contratacao'] = int(input('Ano de contratação: '))
    funcionario ['salario'] = float(input('Salário atual : '))
    funcionario ['aposentadoria'] = (funcionario['contratacao'] - funcionario['Ano de nascimento'] )+ 35

for k,v in funcionario.items():
    print(f'{k} : {v}')

