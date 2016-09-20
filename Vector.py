#Encoding: UTF-8(
#Autor: Oswaldo Morales Rodriguez A01378566
#Conociendo magnitud y angulo, graficar

from Graphics import *
def main():
    magnitud=int(input("Magnitud"))
    angulo=int(input("Angulo"))
    t=Arrow((0,300),0)
    dibujarPlano(t)
    dibujarVector(magnitud,angulo,t)
    
def dibujarPlano(t):
    v=Window("Vector",800,600)
    t.penDown()
    t.draw(v)
    t.forward(800)
    t.rotate(180)
    t.penUp()
    t.forward(400)
    t.rotate(90)
    t.penDown()
    t.forward(300)
    t.rotate(180)
    t.forward(600)
    t.rotate(180)
    t.forward(300)
    t.rotate(90)
    
def dibujarVector(magnitud,angulo,t):
    t.rotate(angulo)
    t.forward(magnitud)
main()
    