frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na aula".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A última letra A apareceu {}".format(frase.rfind("A")+1))

