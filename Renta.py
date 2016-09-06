#encoding: UTF-8
# Autor: Adrin E. Tllez Lpez
# 

def numeroEstrenos(estrenos):
    numero = estrenos * 45.00
    return numero
    
def numeroNormales(normales):
    num = normales * 27.00
    return num
     
def calcularRenta(estrenos, normales):
    Est = numeroEstrenos(estrenos)
    Nor = numeroNormales(normales)
    totalPago = Est + Nor
    return totalPago

def main():
    estrenos = int(input("Peliculas de estreno"))
    normales = int(input("Peliculas normales"))
    d = calcularRenta(estrenos, normales)
    print ("Peliculas de estreno rentadas:", estrenos)
    print ("Peliculas normales rentadas:", normales)
    print ("Total a Pagar: $", d)
    
    
    
main()