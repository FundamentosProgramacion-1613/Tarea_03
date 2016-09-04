# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Cálculos de un círculp

from math import pi

# Función que calcula el diametro de un círculo a partir de su radio
def calcularDiametro(radio):
    diametro = 2*radio
    return diametro

# Función que calcula circunferencia o perimetro a partir de su radio
def calcularCircunferencia(radio):
    circunferencia = pi*radio*2
    return circunferencia

# Función que calcula el área de un círculo a partir de su radio
def calcularArea(radio):
    area = pi*radio**2
    return area
    
def main():
    radio = float(input("Escribe el radio del círculo"))
    diametro = calcularDiametro(radio)
    circunferencia = calcularCircunferencia(radio)
    area = calcularArea(radio)
    print("Círculo con radio: ", format(radio, ".1f"))
    print("Diametro: ", format(diametro, ".2f"))
    print("Circunferencia: ", format(circunferencia, ".2f"))
    print("Área: ", format(area, ".2f"))
main()