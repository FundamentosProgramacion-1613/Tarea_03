# encoding: UTF-8
#Blanca Flor Calderón Vázquez
#Renta de Peliculas

#Con esta función calcularemos la renta de las pelis que adquirirás
def calcularRenta(numeroEstrenos,numeroNormales):
    totalPago=((numeroEstrenos*45)+(numeroNormales*27))
    return totalPago

def main ():
    estrenos=int(input("Leer el número de peliculas de estreno"))
    normales=int(input("leer el número de peliculas normales"))
    pagoTotal= calcularRenta(estrenos,normales)
    
    print (estrenos)
    print (normales)
    print (pagoTotal)

main()



