# encoding: UTF-8
#Blanca Flor Caldern Vazquez
#Circulo y sus  Cálculos

#Con esta funcion obtendremos el diametro
def diametro(r):
    diametro=2*r
    return diametro
#Con esta funcion obtendremos el valor de la cincunferencia
def longitudDeLaCircunferencia(r):
    circunferencia=2*3.1416*r
    return circunferencia
#Con esta funcion obtendremos el area del circulo
def areaDelCirculo(r):
    area=3.1416*r**2
    return area
def main():
    radio=float(input("Introduce el radio"))
    diametroDelCirculo= diametro(radio)
    circunferenciaDelCirculo= longitudDeLaCircunferencia(radio)
    areaDelCirculoo= areaDelCirculo(radio)
    print ("DiametroDelCirculo",diametroDelCirculo)
    print ("CircunferenciaDelCirculo",circunferenciaDelCirculo)
    print ("AreaDelCirculo",areaDelCirculoo)
main()
