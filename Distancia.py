#encoding: UTF-8
# Autor: Adrin E. Tllez Lpez
#

def calcularRendimientokm(Kr, Gu):
    km = Kr / Gu
    return km
    
def calcularRengimientomi(Kr, Gu):
    Millas = Kr * 0.62137
    Galon = Gu * 0.264172051
    Mil = Millas / Galon
    return Mil
    
def calcularKilometros(kms, Kr, Gu):
    kilometros = kms * Gu
    kilometros = kilometros / Kr
    return kilometros


def main():
    Kr = int(input("Kilometros recorridos"))
    Gu = int(input("Litros de gasolina utilizado"))
    kml = calcularRendimientokm(Kr, Gu)
    migalon = calcularRengimientomi(Kr, Gu)
    print ("Si recorre", Kr, "km con", Gu,"litros de gasolina,")
    print ("El rendimiento en km/l es:", kml)
    print ("El rendimiento en mi/galon es:", migalon)
    kms = int(input("¿Cuantos kilometros vas a recorrer?"))
    final = calcularKilometros (kms, Kr, Gu)
    print ("Para recorrer", kms, "kms., necesitas", final, "litros")
    
main()
    