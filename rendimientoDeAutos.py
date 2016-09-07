#encoding: UTF-8

# Autor: Marina Itzel Haro Hernndez, A01373471
# Calcula el rendimiento de un automóvil en kilómetros/litro, en millas/galón y calcula la gasolina que se ocupa dependiendo de los kilómetros


def convertirKmAMillas(km, milla):
    milla = 1.609344
    kmAMillas = km / milla
    return kmAMillas
    
def convertirLitrosAGalones(litros, galon):
    galon = 0.264172051
    litrosAGalones = litros * galon
    return litrosAGalones
    
def calcularRendimientoKmLitros(km, litros):
    rendimientoKmLitros = km / litros
    return rendimientoKmLitros

def calcularLitrosQueNecesitara(kmARecorrer, litros, km):
    litrosQueNecesitara = (kmARecorrer * litros) / km
    return litrosQueNecesitara
    
def main():
    km = int(input("Kilometros recorridos"))
    litros = int(input("Litros de gasolina utilizados"))
    milla = 1.609344
    galon = 0.264172051
    rendimientoKmLitros = km / litros
    kmAMillas = convertirKmAMillas(km, milla)
    litrosAGalones = convertirLitrosAGalones(litros, galon)
    rendimientoMillasGalones = kmAMillas / litrosAGalones
    print("Si recorre", km, "km con", litros, "litros de gasolina,")
    print("El rendimiento en km/l es: %.2f" % (rendimientoKmLitros))
    print("El rendimiento en mi/galon es: %.2f" % (rendimientoMillasGalones))
    kmARecorrer = int(input("¿Cuátos kilómetros vas a recorrer?"))
    litrosQueNecesitara = calcularLitrosQueNecesitara(kmARecorrer, litros, km)
    print("Para recorrer", kmARecorrer, "kms., necesitas %.2f" % (litrosQueNecesitara), "litros")
    
main()