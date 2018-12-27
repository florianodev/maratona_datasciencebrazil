import module.MyLib as ml


lado= ml.entradaFloat("Digite o valor do lado do quadrado: ")

area=0
try:
    area= float(lado)**2
    dobro = area *2
except Exception as err:
    print("Erro no calculo:",err)
print("A área deste quadrado é:",area," e o dobro:",dobro)