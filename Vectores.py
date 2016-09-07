#encoding: UTF-8
#Autor: Diego Perez AKA DiegoCodes
#GraficaVectores
from Graphics import *

#dibuja cuadrantes
def quadrants(win):
    line0 = Line((0,270),(960,270))
    line0.color = Color("green")
    line0.draw(win)
    
    line1 = Line((480,0),(480,960))
    line1.color = Color("green")
    line1.draw(win)

#dibuja vector
def vector(t,win,magnitude):
    t.draw(win)
    t.penDown()
    t.pen.color = Color("yellow")
    t.forward(magnitude)
    
def main(): 
    magnitude = float(input("Escriba Magnitud del vector"))
    angle = float(input("Escriba angulo del vector"))
    
    win = Window("Vectors",960,540)
    win.setBackground(Color('black'))
    
    t = Arrow((480,270),angle)
        
    vector(t,win,magnitude)
    
    quadrants(win)
    
    
main()              