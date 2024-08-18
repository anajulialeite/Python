real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 5.47
euro = real / 6.04
print("Com quantos R${:.2f} você pode comprar, US${:.2f}, €{:.2f}".format(real, dolar, euro))
