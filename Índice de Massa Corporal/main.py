peso = float(input("Qual é o seu peso? (kg): "))
altura = float(input("QAual é a sua altura? (m) "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO do peso normal")
elif 18.5 <= imc < 25:
    print("Parabéns, você está na faixa de peso NORMAL")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE!")
elif imc >= 40:
    print("Cuidado, você está em OBESIDADE MÓRBIDA!")
