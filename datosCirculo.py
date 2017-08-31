#Oscar Zuñiga Lara     A01654827

import math

def diametroCirculo(radio): #Funcion que calcula diametro
    diametro = radio * 2
    return  diametro

def longCircunferencia(radio):  #Función que calcula circunferencia
    long = radio * 2 * math.pi
    return  long
def areaCirculo(radio):  #Función que calcula area de el circulo
    area = math.pi *radio ** 2
    return  area

radio = int(input("Inserte Radio"))  #pide el radio

longCircunferencia = longCircunferencia(radio)
diametroCirculo = diametroCirculo(radio)
area = areaCirculo(radio)
                                        #Invoca las funciones

print("El diametro de el circulo es de: " , diametroCirculo , ".")
print("La circunferencia de el circulo es de: " , longCircunferencia ,  "." )
print("El area de el circulo es de: " , area , ".")

                                            #Imprime los datos