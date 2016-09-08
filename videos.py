#encoding:UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: programa que calcula el total en una tienda de renta de peliculas

#Inicio

#Declaramos la función que calculará el costo
def calcularRenta(numeroEstrenos, numeroNormales):
    totalPago= (45*numeroEstrenos) + (27*numeroNormales) #Hacemos la suma de los costos
    return totalPago
#Declaramos nuestra función principal
def main():
    estrenos = int(input("¿Cuántos estrenos rentaste?"))#Pedimos el número de estrenos rentados
    normales = int(input("¿Cuántas normales rentaste?"))#Pedimos el número de películas normales
    res = calcularRenta(estrenos, normales) #Llamamos la función
    print ("""Rentaste: %d estrenos, %d normales.
    El total es de: $ %.2f""" %(estrenos,normales,res)) #Imprimimos
main()
#Fin