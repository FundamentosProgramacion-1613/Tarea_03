

from Graphics import *

def dibujarPlano(tortuga):
    tortuga.penUp()
    tortuga.rotate(270)
    tortuga.forward(50)
    tortuga.rotate(90)
    tortuga.penDown()
    tortuga.forward(800)
    tortuga.rotate (180)
    tortuga.forward(400)
    tortuga.rotate(90)
    tortuga.forward(400)
    tortuga.rotate (180)
    tortuga.forward(800)
    tortuga.rotate (180)
    tortuga.forward(400)
    tortuga.rotate(90)
    
def dibujarLinea(tortuga, magnitud, angulo):
    tortuga.rotate(angulo)
    tortuga.forward(magnitud)
    

def main ():
    magnitud = int(input("Magnitud"))
    angulo = int(input("Angulo"))
    ventana = Window ("Tortuga", 600, 600)
    tortuga = Arrow ((300, 300), 0)
    tortuga.draw(ventana)
    tortuga.penDown()
    dibujarPlano (tortuga)
    dibujarLinea(tortuga, magnitud, angulo)
    
    
main()
    