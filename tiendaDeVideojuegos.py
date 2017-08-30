#Oscar Zuñiga Lara,   A01654827

def main(juegosNormales, juegosEstreno):
    total = (juegosNormales * 27 + juegosEstreno * 45)
    return total

juegosNormales = int(input("Inserte juegos Normales"))
juegosEstreno = int(input("Inserte juegos Estreno"))

total = main(juegosNormales , juegosEstreno)

print("El costo total es de " , total)