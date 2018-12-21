

print("Digite quanto você ganha por hora?")
hh = input()
print("Digite quantidade de horas trabalhadas")
ht=input()

try:
    hh=float(hh)
    ht=int(ht)
    valor = hh*ht
    print("Você vai receber:",valor)
except Exception:
    print("Erro no calculo")    

