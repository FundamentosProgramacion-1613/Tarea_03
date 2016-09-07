#encoding: utf-8
#autor: Allan Sánchez Iparrazar
#Tienda de videos

def calcularRenta(numeroEstrenos, numeroNormales):
    totalPago = (numeroEstrenos*45)+(numeroNormales*27)
    return totalPago


def main():
    estrenos = int(input("Número de películas de estrenos"))
    normales = int(input("Número de películas normales"))
    totalPago = calcularRenta(estrenos,normales)
    
    print ("Películas de estreno rentadas:",estrenos)
    print ("Películas normale rentadas:",normales)
    print ("Total a pagar $%.2f "%(totalPago))


main()