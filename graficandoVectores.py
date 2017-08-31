#Oscar Zuñiga Lara     A01654827

import  turtle
grados = float(input("Introduzca los grados de el angulo:"))
magnitud = float(input("Introduzca magnitud:"))
                                                    #pide los datos
def vector(grados , magnitud):   #función que dibuja los vectores
    turtle.left(grados)
    turtle.forward(magnitud)
    turtle.exitonclick()

dibujar = vector(grados , magnitud)   #dibuja el vector
