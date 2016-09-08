#encoding:UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: programa que gráfica un vector

#Inicio
from Myro import *
from Graphics import *

def dibujarPlano(g): #Dibuja Plano Cartesiano
    p= Arrow((250,0), 270)
    p.draw(g)
    p.penDown()
    p.forward(500)
    p.penUp()
    p.moveTo(0,250)
    p.rotate(90)
    p.penDown()
    p.forward(500)

def dibujarVector(g,teta,magnitud): #Dibuja el vector dado
    t= Arrow((250,250), teta)
    t.draw(g)
    t.penDown()
    t.forward(magnitud)

def main(): #Función principal
    m= float(input("Introduce la magnitud del vector"))
    t= float(input("Introdu5ce el angulo del vector"))
    g= Window('Vector',500,500)
    dibujarPlano(g)
    dibujarVector(g,t,m)

main()