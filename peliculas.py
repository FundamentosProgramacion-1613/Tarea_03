#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 1

Estrenos=int(45)
Normales= int(27)
    
def calcularRenta(numeroEstrenos,numeroNormales):
    total= (numeroEstrenos) + (numeroNormales)
    return total
             
def main():  
    mestrenos= int(input("Numero de peliculas de estreno"))
    mnormales= int(input("Numero de peliculas normales"))
    print ("Numero de peliculas de estreno son: ",mestrenos)
    print ("Numero de peliculas normales son: ",mnormales)
    numeroEstrenos= (mestrenos * Estrenos)
    numeroNormales= (mnormales * Normales)
    total1 = calcularRenta(numeroEstrenos,numeroNormales)
    print ("El total a pagar es de:",total1)
    
main()