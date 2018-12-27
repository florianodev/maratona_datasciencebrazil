import module.MyLib as ml

hh = ml.entradaFloat("Quanto ganha por hora? ")
ht = ml.entradaFloat("Horas trabalhadas no mês? ")

salario = hh*ht;

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

liquido = salario - ir - inss - sindicato

print("+ Salário Bruto: R$ %.2f" % salario)
print("- IR: R$ %.2f" % ir)
print("- INSS:R$ %.2f" % inss)
print("- Sindicato:R$ %.2f" % sindicato)
print("= Salário liquido: R$ %.2f" % liquido)
