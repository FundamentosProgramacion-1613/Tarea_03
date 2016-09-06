#encoding: UTF-8
#Autor: Jesus Perea
#Datos de un círculo

def calcularDiametro (r):
    diametro = r * 2
    return diametro
    
def calcularLongitud (r):
    longitud = (r*2) * 3.1416
    return longitud

def calcularArea (r):
     area = (r**2) * 3.1416
     return area        
    
def main():
    radio = float(input("Tecle el radio del circulo"))
    print ("Radio de un circulo:",radio)
    print ("Diametro:", calcularDiametro(radio))
    print ("Circunferencia:", calcularLongitud(radio))
    print ("Area:",calcularArea(radio))
    
main()
   