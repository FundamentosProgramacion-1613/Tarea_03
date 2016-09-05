#encoding: UTF-8
#Autor: Aldo Fuentes - A01373294
#Calcular datos de un circulo

from math import *

def diametro(radio):
    diametro = 2 * radio
    return diametro

def circunferencia(diametro):
    circunferencia = pi * diametro
    return circunferencia
    
def area(radio):
    area = pi * radio**2
    return area
    
def main():
    radio = float(input("Radio del circulo"))
    d = diametro(radio)
    c = circunferencia(d)
    a = area(radio)
    print("Circulo con radio: ", radio)
    print("Diametro: ", "%.2f" % d)
    print("Circunferencia: ", "%.2f" % c)
    print("Area: ", "%.2f" % a)
    
main()