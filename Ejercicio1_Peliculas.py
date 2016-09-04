# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Renta de películas

# Función que calcula el costo total de la renta de los videos
def calcularRenta(numeroEstrenos, numeroNormales):
    total = numeroEstrenos*45+numeroNormales*27
    return float(total)
    
def main():
    estrenos = int(input("Películas de Estreno"))
    normales = int(input("Películas Normales"))
    costo = calcularRenta(estrenos, normales)
    print("Películas de estreno rentadas: ", estrenos)
    print("Películas normales rentadas: ", normales)
    print("Total a pagar: $", format(costo, ".2f"), sep="")
main()