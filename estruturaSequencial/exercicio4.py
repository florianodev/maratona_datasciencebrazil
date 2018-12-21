print("Digite a primeira nota")
nota1= input()
print("Digite a segunda nota")
nota2=input()
print("Digite a terceira nota")
nota3=input()
print("Digite a quarta nota")
nota4=input()
media = 0
try:
    media = float(nota1)+float(nota2)+float(nota3)+float(nota4)/4
except Exception as err:
    print("Erro no calculo:",err)
print("A média é:",media)