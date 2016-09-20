#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 2

import math

def calcularDiametro(r):
    diametro= r * 2
    return diametro
    
def calcularPerimetro(diametro):
    p= math.pi * diametro
    return p
    
def calcularArea(r):
    a= math.pi * (r)**2
    return a
    
def main():
    radio= float(input("¿Cuanto mide el radio?"))
    diam= calcularDiametro(radio)
    peri= calcularPerimetro(diam)
    area= calcularArea(radio)
    print ("El radio del circulo es: ",radio)
    print ("El diametro del circulo es: ",diam)
    print ("La circunferencia del circulo es: ",peri)
    print ("El area del circulo es: ", area)
        
main()   