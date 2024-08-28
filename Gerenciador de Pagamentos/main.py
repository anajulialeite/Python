print("Lojas Guanabara")
preço  = float(input("Preço das compras: R$"))
print('''Formas de pagamento
[ 1 ] à vista dinheirfo/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(totalparc, parcela))
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
else:
    total = 0
    print("Opção inválida de pagamento. tente novamente!")
print("Sua compra de R$ {:.2f} vai custar {:.2f} no final".format(preço, total))
