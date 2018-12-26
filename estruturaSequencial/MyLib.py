
#***************************************************

def entradaInt(descErro="O valor digitado não é um número INTEIRO",legenda="Digite um número inteiro:"):

    while True:
        try:
            resp = int(input(legenda))
        except ValueError:
            print(descErro)
            continue
        else:
            break
    return resp

#***************************************************

def entradaFloat(descErro="O valor digitado não é um número REAL",legenda="Digite um número real:"):

    while True:
        try:
            resp = float(input(legenda))
        except ValueError:
            print(descErro)
            continue
        else:
            break
    return resp

