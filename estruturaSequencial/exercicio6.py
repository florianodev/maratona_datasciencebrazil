import math
import module.MyLib as ml

raio= ml.entradaFloat("Digite o valor do raio: ")

area=0
try:
    area= math.pi*float(raio)**2
except Exception as err:
    print("Erro no calculo:",err)
print("A área deste raio é:",area)