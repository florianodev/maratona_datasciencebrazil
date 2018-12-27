import module.MyLib as ml

numInt1 = ml.entradaInt("Digite um número inteiro: ")
numInt2 = ml.entradaInt("Digite outro número inteiro: ")
numReal = ml.entradaFloat()

produto = (numInt1*2)*(numInt2/2)
soma = (numInt1*3)+numReal
cubo = numReal**3

print("O produto do dobro do primeiro com a metade do segundo é:",produto)
print("A soma do triplo do primeiro com o terceiro:",soma)
print("O terceiro elevado ao cubo : ",cubo)