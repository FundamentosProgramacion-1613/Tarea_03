#Encoding: UTF-8
#Autor: Oswaldo Morales Rodriguez A01378566
#Sabiendo el número de peliculas rentadas obtenr el precio

def main():
    estrenos=int(input("Total de estrenos rentados"))
    normales=int(input("Total de estrenos normales"))
    renta=calcularRenta(estrenos,normales)
    print("Peiculas de estreno rentadas:",estrenos,"Peliculas normales rentadas:",normales,"Total a pagar $",renta)

def calcularRenta(estrenos,normales):       #Con esta funcion se consigue el total a pagar
    totalEstrenos=estrenos*45
    totalNormales=normales*27
    renta=totalEstrenos+totalNormales
    return renta
  
main()