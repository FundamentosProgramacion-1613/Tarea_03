
#encoding: UTF-8

#Autor: José Javier Rodríguez Mota
#Descripción: Programa que dibuja un vector

#Importamos gráficos
from Graphics import *
#Inicio
def dibujarCuadricula(l,c,v):
    x =Line((-l,c),(l,c))
    x.color = Color("green")
    x.draw(v)
    y =Line((c,-l),(c,l))
    y.color = Color("green")
    y.draw(v)
def dibujarVector(g,v,m):
    g.draw(v)
    g.penDown()
    g.pen.color = Color("yellow")
    g.forward(m)
def dibujarCuadrado(x,y,m,v):
    xv = Line((x,y),(m,y))
    xv.color = Color("red")
    xv.draw(v)
    yv = Line((x,y),(x,m))
    yv.color = Color("red")
    yv.draw(v)
#Definimos main
def main():
    #Pedimos los valores de entrada iniciales
    m=float(input("Magnitud del vector"))
    a=float(input("Ángulo del vector en grados"))
    l=m*2
    #Iniciamos nuestra flecha y ventana
    v= Window("Vector",l,l)
    v.setBackground(Color("black"))
    g= Arrow((m,m),a)
    #Dibujamos nuestra cuadrícula
    dibujarCuadricula(l,m,v)
    #Lo hacemos caminar
    dibujarVector(g,v,m)
    x1=g.getX()
    y1=g.getY()
    dibujarCuadrado(x1,y1,m,v)    

#Iniciamos el código    
main()
#Fin