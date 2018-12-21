print("Digite o valor em metros")
med= input()

medida=0
try:
    medida= float(med)*100
except Exception as err:
    print("Erro no calculo:",err)
print(med,"m equivale a:",medida,'cm')