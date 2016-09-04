#Encoding: UTF-8
#Autor: Oswaldo Morales Rodriguez A01378566
#Sabiendo el radio obtener el diametro, la circunferencia y el area

from math import pi
def main():
    radio=int(input("Medida del radio"))
    diametro=calcularDiametro(radio)
    circunferencia=calcularCircunferencia(radio)
    area=calcularArea(radio)
    print("El radio es",radio,"El diametro es:",diametro,"La circunferencia es",circunferencia,"El area es",area)


def calcularDiametro(radio):  #Aqui se calcula el diametro
    diametro=radio*2
    return diametro

def calcularCircunferencia(radio):   #Aqui se calcula la circunferencia
    circunferencia=2*pi*radio
    return circunferencia 

def calcularArea(radio):    #Aqui se calcula el area
    area=pi*(radio**2)
    return area

main()