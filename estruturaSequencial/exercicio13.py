import module.Peso as p
import module.MyLib as ml

print("Peso ideal para você?")

altura = ml.entradaFloat("Digite sua altura: ")

texto= "O peso ideal para"
peso = p.Peso(altura)

print(texto,"homem é",peso.homem())
print(texto,"mulher é",peso.mulher())