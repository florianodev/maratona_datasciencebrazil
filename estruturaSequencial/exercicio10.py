def conversor(celsius):
    return (celsius*9/5)+32

print("Conversor de temperatura de Celsius para Fahrenheit\n")
print("Digite o valor em Celsius")
temp = input()
fahrenheit=0
try:
    fahrenheit = conversor(float(temp))
except Exception as err:
    print("Erro no calculo:",err)
print(temp,"Celsius equivale a:",fahrenheit,"fahrenheit")