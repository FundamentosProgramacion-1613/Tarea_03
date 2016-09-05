#encoding: UTF-8
#Autor: Aldo Fuentes - A01373294
#Calcular precio de renta de peliculas.



def calcularRenta(numeroEstrenos, numeroNormales):
    numeroEstrenos *= 45
    numeroNormales *= 27
    totalPago = numeroEstrenos + numeroNormales
    return totalPago

def main():
    estrenos = int( input("Peliculas de estreno"))
    normales = int( input("Peliculas normales"))
    total = calcularRenta(estrenos, normales)
    print("Peliculas de estreno rentadas: ", estrenos)
    print("Peliculas normales rentadas: ", normales)
    print("Total a pagar: $", "%.2f" % total)

main()    