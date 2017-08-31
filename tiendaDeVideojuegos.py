#Oscar Zuñiga Lara,   A01654827

def main(juegosNormales, juegosEstreno):#Función que calcula el costo
    total = (juegosNormales * 27 + juegosEstreno * 45)
    return total

juegosNormales = int(input("Inserte juegos Normales")) #Pide juegos normales
juegosEstreno = int(input("Inserte juegos Estreno")) #Pide juegos estreno

total = main(juegosNormales , juegosEstreno) #Invoca el costo

print("El costo total es de " , total) #Imprime costo