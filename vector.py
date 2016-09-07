#encoding: UTF-8
#Blanca Flor Caldern Vazquez
#vectores

from Graphics import*
from math import*

#Con esta función convertiremos radianes a grados
def convertirRadianesAGrados(rad):
    grados=(rad*180)/3.1416
    return grados
def main():
    magnitud=int(input("ingresa la magnitud"))
    angulo=int(input("ingresa el ángulo"))
    anguloG=convertirRadianesAGrados(angulo)
   
    
    v=Window("Top-Down",800,800)
    t=Arrow((0,400),90)
    t.penDown()
    t.draw(v)
    t.forward(800)
    t.penUp()
    t.rotate(180)
    t.forward(400)
    t.rotate(90)
    t.penDown()
    t.forward(400)
    t.rotate(180)
    t.forward(800)
    t.penUp()
    t.rotate(90)
    t.penDown()
    t.rotate(anguloG)
    t.forward(magnitud)
    
    

main()
