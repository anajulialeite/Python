from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu {} em {} anos em {}".format(nasc, idade, atual))
if idade == 18:
     print("Voc~e tem que se alistar, IMEDIATAMENTE!")
elif idade < 18:
     saldo = 18 - idade
     print("ainda falta {} anos para o alistamento".format(saldo))
     ano = atual + saldo
     print("Seu alistamento será em {} ano.".format(ano))
elif idade > 18:
     saldo = idade - 18
     print("Você já deveria ter se alistado há {} anos".format(saldo))
     ano = atual - saldo
     print("Seu alistamento foi em {} ano.".format(ano))
