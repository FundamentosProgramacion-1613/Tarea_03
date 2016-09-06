#encoding: UTF-8
#Autor: Jesús Perea Villegas    
#Calcular total a pagar de una tienda de videos

def calcularRenta(numeroEstrenos, numeroNormales):
    totalPago = numeroEstrenos + numeroNormales    
    return totalPago
    
def main ():   
    estrenos = int(input("Número de estrenos")) * 45
    normales = int(input("Número de peliculas normales")) * 27
    print ("Peliculas de estreno",estrenos)
    print ("Peliculas normales",normales) 
    total = calcularRenta(estrenos, normales)
    print ("Total a pagar:",total)
       
main()    
