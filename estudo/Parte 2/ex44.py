print("PAGAMENTO")
produto = float(input("PRODUTO R$: "))
print("")
print("As opções de pagamento disponíveis são:")
print("[1]PIX")
print("[2]CARTÃO DE DÉBITO")
print("[3]CARTÃO DE CRÉDITO")
forma = int(input("Qual será a forma de pagamento:"))
if forma == 1:
    desconto = produto * 0.9
    print(f"Com um desconto, o produto sairá por R${desconto:.2f}")
elif forma == 2:
    desconto = produto*0.95
    print(f"Com um desconto,o produto sairá por R${desconto:.2f}")
else:
    print("Em quantas vezes você deseja parcelar?")
    print("[1]2x")
    print("[2]3x ou mais")
    parcela = int(input("Informa a opcão escolhida:"))
    if parcela == 1:
        print(f"O valor a ser pago será de {produto}")
    else:
        juros = (produto*1.2)
        quantParcela = int(input("Em quantas parcelas você gostaria?"))
        print(f"O valor a ser pago será de R${juros:.2f}")
        divisao = juros/quantParcela
        print(f"Fazendo em {quantParcela} parcelas,o total será de R${divisao:.2f} por parcela")