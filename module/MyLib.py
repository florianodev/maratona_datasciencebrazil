
#***************************************************

def entradaInt(legenda="Digite um número inteiro:",descErro="O valor digitado não é um número INTEIRO"):

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

def entradaFloat(legenda="Digite um número real:",descErro="O valor digitado não é um número REAL"):

    while True:
        try:
            resp = float(input(legenda))
        except ValueError:
            print(descErro)
            continue
        else:
            break
    return resp

