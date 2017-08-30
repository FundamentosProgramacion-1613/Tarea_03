#Oscar Zuñiga Lara     A01654827

import math

def diametroCirculo(radio):
    diametro = radio * 2
    return  diametro

def longCircunferencia(radio):
    long = radio * 2 * math.pi
    return  long
def areaCirculo(radio):
    area = math.pi *radio ** 2
    return  area

radio = int(input("Inserte Radio"))

longCircunferencia = longCircunferencia(radio)
diametroCirculo = diametroCirculo(radio)
area = areaCirculo(radio)

print("El diametro de el circulo es de: " , diametroCirculo , ".")
print("La circunferencia de el circulo es de: " , longCircunferencia ,  "." )
print("El area de el circulo es de: " , area , ".")
