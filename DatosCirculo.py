#encoding: UTF-8
#Autor: Diego Perez AKA DiegoCodes
#Calculador de Datos De Un Circulo
from math import pi

#Utilza formulas matematicas del circulo para definir las variables correspondientes
def circleData(radius):
    diam = radius*2
    circunf = diam*pi
    area = (radius**2)*pi
    return diam,circunf,area
    
def main():
    radius = int(input("Introducir radio del circulo"))
    (diam,circunf,area) = circleData(radius)
    print("Circulo con radio:%.2f" %radius)
    print("Diametro:%.2f" %diam)
    print("Circunferencia:%.2f" % circunf)
    print("Area:%.2f" % area)
main()