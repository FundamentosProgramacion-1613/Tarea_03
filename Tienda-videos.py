#encoding: UTF-8
#Autor: Lenin Silva Gutiérrez, A01373214
#Calcula el pago total de la renta de videos

#obtiene el total de la renta
def calcularRenta(estrenos,normales):
    total=(estrenos*45)+(normales*27)
    return total
    
def main():
    estrenos=int(input("Películas de estreno rentadas")) #lee estrenos rentados
    normales=int(input("Películas normales rentadas"))#lee películas normales rentadas
    total=calcularRenta(estrenos,normales)
    print ("Películas de %s rentadas: %d"% ("estreno", estrenos))
    print ("Películas %s rentadas: %d" % ("normales", normales))
    print ("Total a pagar: $%.2f"% (total))
    
main()
