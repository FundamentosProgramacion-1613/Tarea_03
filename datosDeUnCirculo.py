#encoding: UTF-8

# Autor: Marina Itzel Haro Hernndez, A01373471
# Lee el radio de un círculo e imprime el dimetro, la longitud de la circunferencia y el área del círculo.



def calcularDiametro(radio):
    diametro = radio * 2
    return diametro
    
def calcularLongitud(radio, pi):
    longitud = (radio*2)*pi
    return longitud
    
def calcularArea(radio, pi):
    area = pi*(radio**2)
    return area
    
def main():
    pi = 3.14159265359
    radio = float(input("Escribe el radio del círculo"))
    diametro = calcularDiametro(radio)
    longitud = calcularLongitud(radio, pi)
    area = calcularArea(radio, pi)
    print("Circulo con radio:", radio)
    print ("Diametro:", diametro)
    print("Circunferencia: %.2f" % (longitud))
    print("Area: %.2f" % (area)) # %.2f sirve para imprimir cierto número de decimales en este caso sólo 2
    
main()
    
