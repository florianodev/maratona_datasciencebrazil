import module.MyLib as ml

print("Calcule o peso ideal pela sua altura")

altura = ml.entradaFloat("Digite sua altura: ")

calculo = (72.7*altura)-58

print("Seu peso idela é: ",calculo)