# Oscar Zuñiga Lara     A01654827

import math

def main():
    r = radio()
    diametrov = diametro(r)
    area = areaC(r)
    print("El radio es de ", r ,".")
    print("El diametro es de ", diametrov)
    print("El area es de ", area)


def radio():
    radio = int(input("Insert Radio"))
    return radio

def diametro(radio):
    diametrov = radio * 2
    return diametrov
def areaC(radio):
    areav = math.pi * radio ** 2
    return areav

main()