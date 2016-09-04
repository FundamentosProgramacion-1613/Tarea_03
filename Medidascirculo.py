#encoding: UTF-8
#Karla Valeria Alcantara Duarte A01373164
#Calcular medidas de un circulo

from math import *

def calcularDiametro(radio): #Calcula diametro del circulo
    diametro = radio*2
    return diametro
    
def calcularCircunferencia(diametro): #Calcula circunferencia del circulo
    circunferencia = pi*diametro
    return circunferencia
    
def calcularArea(radio): #Caluca radio del circulo
    area = pi*radio**2
    return area
    
def main():
    radio = float(input("Introduce el radio"))
    diametro = calcularDiametro(radio)
    circunferencia = calcularCircunferencia(diametro)
    area = calcularArea(radio)
    print("El radio es:",radio)
    print("El diametro es:",("%.02f")%(diametro))
    print("La circunferencia es:",("%.02f")%(circunferencia))
    print("El área es:",("%.02f")%area)
    
main()