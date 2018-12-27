import module.MyLib as ml

PESO_PERMITIDO = 50

peso = ml.entradaFloat("Digite o peso: ")
multa = 0
if peso > 50:
   multa = peso%PESO_PERMITIDO*4.0

print("A multa para este peso é R$ %.2f" % multa)


