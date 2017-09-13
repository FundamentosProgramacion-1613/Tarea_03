#Oscar Zuñiga Lara,   A01654827


def main():
    imprimirCostos()

def numerosEstrenos():
    estreno = int(input("Introduzca Estrenos: "))
    return estreno

def numeroNormales():
    normales = int(input("Introduzca Normales: "))
    return normales

def calcularRenta(normales,estreno):
    rentaT = estreno * 45 + normales * 27
    return rentaT

def imprimirCostos():
    x = calcularRenta(numeroNormales(),numerosEstrenos())
    print(x)

main()



