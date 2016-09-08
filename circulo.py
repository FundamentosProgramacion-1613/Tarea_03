#encoding: utf-8
#autor: Allan Snchez Iparrazar
#Circulo

def calcularArea(r):
    area = 3.14*r*r
    return area

def calcularDiametro(r):
    diametro = r*2
    return diametro
    
def calcularPerimetro(r):
    perimetro = 2*3.14*r
    return perimetro

def main():
    r = float(input("Ingresa el radio de un círculo"))
    area = calcularArea(r)
    diametro = calcularDiametro(r)
    perimetro = calcularPerimetro(r)
    print("Radio del circulo:%.1f"%r)
    print("Área del circulo:%.2f"%area)
    print("Diametro del circulo:%.2f"%diametro)
    print("Perimetro del circulo:%.2f"%perimetro)
main()