volta = 0
lista =[]
for c in range(0,3):
     n = int(input("Insira um valor : "))
     #se estivermos na primeira volta (c==0) ou se o valor digitado for maior que o último valor que tinha sido
     #inserido na lista (len(lista)-1 , aqui to pegando o total da lista e subtraindo um,pra pegar o útimo
     # valor da lista
     if c ==0 or n > lista[-1]:
         lista.append(n)
         #caso uma das duas condições seja real,não tem necessidade de varrer a lista
     else:
         #comeco a varrer a lista,então enquanto posição for menor do que a quantidade de numeros da lista,ela
         #vai continuar varrendo
         pos = 0
         while pos < len(lista):
             #caso o valor n seja menor ou igual ao valor que está dentro da lista em determinada posição
             #esse valor n irá assumir aquele específico lugar através do lista.insert
             if n <= lista[pos]:
                 lista.insert(pos,n)
                 break
             pos+=1
print(lista)