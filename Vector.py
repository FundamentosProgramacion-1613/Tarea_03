#encoding: UTF-8
#Karla Valeria Alcantara Duarte A01373164
#Dibujar un vector

from Graphics import *

def dibujarVector(t,grados, magnitud): #Dibuja el vector del usuario 
    t.pen.color = Color("Blue")
    t.rotate(grados)
    t.forward(magnitud)
    
def dibujarPlano(t,valorx,valory): #Dibujar el plano cartesiano
    t.pen.color = Color("Red")
    t.forward(600)
    t.penUp()
    t.moveTo(300,600)
    t.penDown()
    t.rotate(90)
    t.forward(600)
    t.penUp()
    t.moveTo(300,300)
    t.penDown()
    t.rotate(270)
   
def main():
    v = Window("Vector",600,600)
    t = Arrow((0, 300),0)
    t.draw(v)
    t.penDown()
    dibujarPlano(t,600,600)
    grados = int(input("Introduce el ángulo del vector:"))
    magnitud = int(input("Introduce la magnitud del vector:"))
    dibujarVector(t,grados,magnitud)
    
main()