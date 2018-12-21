def conversor(fahrenheit):
    return (5*(fahrenheit-32)/9)

print("Conversor de temperatura de Fahrenheit para Celsius\n")
print("Digite o valor em Farenheit")
temp = input()
celsius=0
try:
    celsius = conversor(float(temp))
except Exception as err:
    print("Erro no calculo:",err)
print(temp,"F equivale a:",celsius," celsius")