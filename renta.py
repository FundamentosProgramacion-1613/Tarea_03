#encoding: UTF-8
#Karla Valeria Alcantara Duarte A01373164
#Calcular renta de películas 

def calcularRenta(estrenos,normales): #Calcular el pago total por la renta de películas
    totalPago = (estrenos*45)+(normales*27)
    return totalPago
    
def main():
    estrenos = int(input("Introduce  el número de peliculas de estreno"))
    normales = int(input("Introduce el número de películas normales"))
    pago = calcularRenta(estrenos,normales)
    print("Número de estrenos:",estrenos) 
    print("Número de normales:",normales)
    print("Total de pago:",pago)
    
main()