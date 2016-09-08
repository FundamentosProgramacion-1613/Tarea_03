#encoding:UTF-8
#Autor: Carlos E. Carbajal Nogus
#Descripcion: programa que calcula los pagos de un trabajador
#Inicio
def calcularGas_utilizada(km,lts): #Función que calcula la gasolina utilizada
    res1= km/lts
    return res1

def convertirKm(kml): #Función que convierte los kilometros a millas y litros a galones
    res2= (kml*(3.785/1.609344))
    return res2

def calcularGas_necesaria(kr,lr): #Función que calcula al gasolina necesaria para recorrer cierto numero de kilometros
    res3=kr/lr
    return res3

def main(): #Función principal
    k=float(input("¿Cuántos kilometros recooriste?"))
    l=float(input("¿Cuántos litros de gasolina usaste?"))
    u= calcularGas_utilizada(k,l)
    m= convertirKm(u)
    print ("""    En %.2f km utilizaste %.2f litros de gasolina
    El rendimiento es de: %.2f km/l
    o bien:               %.2f mi/g""" %(k,l,u,m))
    r=float(input("¿Cuántos kilometros vas a recorrer?"))
    res= calcularGas_necesaria(r,u)
    print ("""Necesitas: %.2f lts para recorrer %.2f kilometros"""%(res,r))
main()