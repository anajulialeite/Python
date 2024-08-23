#todo método tem parênteses no final do comando
nome = str(input("Qual é o seu nome? "))
if nome == "Gustavo":
    print("Que nome lindo vc tem!")
else:
    print("Seu nome é tão normal!")
print("Bom dia, {}".format(nome))