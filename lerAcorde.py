from notaValor import *
#dado um acorde retornar os valores 
def lerAcorde(acorde):
    return notaValor[acorde]

if __name__ == "__main__":
    print(lerAcorde(input()))
    print(valorNota[3][0])
