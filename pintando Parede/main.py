larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede:"))
área = larg * alt
print("Sua parede tem a dimenssão de {}*{} e sua área é de {}m²".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, você vai precisar de {}l de tinta".format(tinta))