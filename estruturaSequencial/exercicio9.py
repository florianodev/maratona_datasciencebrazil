import module.MyLib as ml

def conversor(fahrenheit):
    return (5*(fahrenheit-32)/9)

print("Conversor de temperatura de Fahrenheit para Celsius\n")

temp = ml.entradaFloat("Digite o valor em Farenheit: ")
celsius=0
try:
    celsius = conversor(temp)
except Exception as err:
    print("Erro no calculo:",err)
print(temp,"F equivale a:",celsius," celsius")