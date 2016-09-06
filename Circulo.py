#encoding: UTF-8
# Autor: Adrin E. Tllez Lpez
#

def calcularDiametro (radio):
    diametro = radio * radio
    return diametro
    
def calcularCircunferencia (radio):
    circunferencia = 2 * radio * 3.1416
    return circunferencia
    
def calcularArea (radio):
    Area = 3.1415 * (radio * radio)
    return Area


def main():
    radio = float(input("Escribe el radio del circulo"))
    diame = calcularDiametro(radio)
    circun = calcularCircunferencia(radio)
    area = calcularArea(radio)
    print ("Radio del circulo:", radio)
    print ("Diametro:", diame)
    print("Circunferencia:", circun)
    print ("Area:", area)

main()
    
    