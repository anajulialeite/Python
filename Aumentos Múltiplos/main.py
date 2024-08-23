salário = float(input("Qual é o salário do funcionário? RS"))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print("Quem ganhava R${:02f} passa a ganhar R${:.2f} agora".format(salário, novo))
