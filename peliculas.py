#encoding:UTF-8
#Ma Fernanda Rodriguez Hrdz
# escribir un programam que reciba el numero de peliculas e imprima el total a pagar

def calcularRenta(numeroEstrenos,numeroNormales):
    numero_de_peliculas = numeroEstrenos + numeroNormales
    total_a_pagar = (numeroEstrenos * 45) + (numeroNormales * 27)
    return total_a_pagar

def main():
    #pidiendo datos
    estrenos = int(input("cuantas peliculas de estreno rentaste"))
    normales = int(input("cuantas peliculas normales rentaste"))
    #llamando a la funcion 
    calcularRenta(estrenos,normales)
    #imprimir valores
    print ("peliculas de estreno rentadas:",estrenos,
    "\npeliculas normales rentadas:",normales,
    "\ntotal a pagar: $",calcularRenta(estrenos,normales))
main()