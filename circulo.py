#encoding:UTF-8
#Ma Fernanda Rodriguez Hrdz
#escribir un programam que lea el radio de un circulo e imprima su longitud,area y diametro

#definiendo funsiones
def diametro(radio):
    diametro = radio *2
    return diametro
    
def longitudCirunferencia(radio):
    circunferencia = (radio*2) * 3.14
    return circunferencia 
    
def area(radio):
    area = 3.14 * (radio**2)
    return area

def main():
    radio=float(input("cual es el radio del circulo"))
    #llamando funsiones
    diametro(radio)
    longitudCirunferencia(radio)
    area(radio)
    #imprimiendo funsiones
    print(
    "circulo con radio:",radio,
    "\ndiametro:",diametro(radio),
    "\ncircunferencia:",longitudCirunferencia(radio),
    "\narea:",area(radio)
    )

    
main()