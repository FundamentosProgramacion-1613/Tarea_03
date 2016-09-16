#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°1 de la tarea 3

def calcularRenta(numeroEstrenos,numeroNormales):
    totalPago = numeroEstrenos + numeroNormales
    return float(totalPago) #00.00
    
def main() :
    numeroEstrenos = int(input("Peliculas de estreno"))
    numeroNormales = int(input("Peliculas normales"))
    totalPago = calcularRenta(numeroEstrenos,numeroNormales)
    print("Peliculas de estreno rentadas:" ,numeroEstrenos)
    print("Pelucilas normales rentadas:" ,numeroNormales)
    print("Total a pagar:$", format(totalPago), sep="") #http://stackoverflow.com/questions/22116482/python-syntax-help-sep-t

main()