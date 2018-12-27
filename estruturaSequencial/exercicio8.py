import module.MyLib as ml


hh = ml.entradaFloat("Digite quanto você ganha por hora?: ")
ht=ml.entradaInt("Digite quantidade de horas trabalhadas: ")

try:
    hh=float(hh)
    ht=int(ht)
    valor = hh*ht
    print("Você vai receber:",valor)
except Exception:
    print("Erro no calculo")    

