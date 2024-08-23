#toda vez que for utilizar uma cor ele começa com \033[m
#style - estilo (0)
#text - texto (33)
#background - fundo (44)
#\033[0;33;44m] modo de declarar
#Style:
#0 none, 1 bold, 4 underline, 7 negative
#30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 azul, 37 cinza
#40 branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 azul, 47 cinza

#print("\033[4;30;45mOlá, Mundo!\033[m")

#a = 3
#b = 5
#print("Os valores são \033[32m{}\033[m e \033[34m{}\033[m!!!".format(a, b))

#nome = "Ana Júlia"
#print("Olá, muito prazer em te conhecer, {}{}{}!!!".format("\033[4;35m", nome, "\033[m"))

nome = "Ana Júlia"
cores = {"limpa":"\033[m",
         "vermelho":"\033[31m",
         "amarelo":"\033[33m",
         "pretoebranco":"\033[7;40m"}
print("Olá, muito prazer em te conhecer, {}{}{}!!!".format(cores["pretoebranco"], nome, cores["limpa"]))
