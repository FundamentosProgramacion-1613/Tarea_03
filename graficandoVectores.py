#Oscar Zuñiga Lara     A01654827

import  turtle
def main():
    grados = float(input("Introduzca los grados de el angulo:"))
    magnitud = float(input("Introduzca magnitud:"))  #pide los datos
    vector(grados,magnitud)

def vector(grados ,magnitud):   #función que dibuja los vectores
    turtle.left(grados)
    turtle.forward(magnitud)
    turtle.exitonclick()

main()

