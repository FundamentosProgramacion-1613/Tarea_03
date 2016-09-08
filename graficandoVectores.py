#encoding: UTF-8
#autor: Allan Sánchez Iparrazar
#Dibuja un vector dado el ángulo
from Graphics import *
   

def dibujarPlano(t): 
    t.penDown()
    t.rotate(270)
    t.forward(800)
    t.penUp()
    t.moveTo(0,400)
    t.penDown()
    t.rotate(90)
    t.forward(800)
    t.penUp()
    
def dibujarVector(vector,magnitud,grados):
    
    vector.penDown()
    vector.rotate(grados)
    vector.forward(magnitud)
    
    

def main():
    v = Window("Plano",800,800)
    t = Arrow((400,0),0)
    t.draw(v)
    vector = Arrow((400,400),0)
    vector.draw(v)
    dibujarPlano(t)
    magnitud = int(input("Ingresa la magnitud de tu vector"))
    grados = int(input("Ingresa el ángulo que tendrá tu vector"))
    dibujarVector(vector,magnitud,grados)
    
    
main()