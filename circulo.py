#encoding:UTF-8
#Autor: Carlos E. Carbajal Nogus
#Descripcion: programa que calcula los datos de un circulo
#Inicio

#Hacemos la función que calculará el diametro
def calcularDiametro(radio):
    diametro=2*radio #se hace la operación para sacar el diametro
    return diametro

#Funcion que calcula el area
def calcularArea(radio,pi):
    area=pi*(radio**2) #se hace el calculo del area
    return area

#Funcion que calcula la circunferencia
def calcularCircunferencia(radio,pi):
    circu=2*pi*radio #calculamos la circunferencia
    return circu

#Hacemos nuestra funcion principal
def main():
    r=float(input("Introduce el radio del circulo"))
    d=calcularDiametro(r)
    c=calcularCircunferencia(r,3.1416)
    a=calcularArea(r,3.1416)
    print ("""    El diametro es de: %.2f
    La circunferencia es de: %.2f
    El area es de: %.2f""" %(d,c,a))
main()
#Fin