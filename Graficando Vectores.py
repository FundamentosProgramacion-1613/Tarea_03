#encoding: UTF-8
#Autor: Jesus Perea 
#Graficando vectores

from Graphics import*

def dibujarCartesiano(w):
    linea1 = Line((300,0),(300,600))
    linea1.draw(w)
    lineaa = Line((0,300),(600,300))
    lineaa.draw(w)
    
def dibujarVector (w,magnitud, angulo):
    f = Arrow ((300,300),0)
    f.draw(w)
    f.rotate(angulo)
    f.penDown()
    f.forward(magnitud)
    f.penUp()
    
def main():
    angulo = int(input("Teclea el ángulo del vector"))
    magnitud = int(input("Teclea la magnitud del vector"))
    w = Window (600,600)
    dibujarVector (w,magnitud,angulo)
    dibujarCartesiano(w)
    
main()    