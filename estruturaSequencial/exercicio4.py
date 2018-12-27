import module.MyLib as ml



nota1= ml.entradaFloat("Digite a primeira nota: ")
nota2=ml.entradaFloat("Digite a segunda nota: ")
nota3=ml.entradaFloat("Digite a terceira nota: ")
nota4=ml.entradaFloat("Digite a quarta nota: ")
media = 0
try:
    media = (float(nota1)+float(nota2)+float(nota3)+float(nota4))/4
except Exception as err:
    print("Erro no calculo:",err)
print("A média é:",media)