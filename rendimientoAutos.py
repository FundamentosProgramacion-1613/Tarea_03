# Oscar Zuñiga Lara    A01654827

def main():
    kmrecorridos = float(input("Inserte kilometros recorridos"))
    litrosconsumidos = float(input("Inserte Litros Consumidos"))
    print(kmL(kmrecorridos, litrosconsumidos))
    print(millGal(kmrecorridos,litrosconsumidos))
    kmArecorrer = float(input("Cuanto quieres viajar"))
    print(litrosnecesarios(kmrecorridos,kmL(kmrecorridos,litrosconsumidos)))

def kmL(km, l):
    rend = km / l
    return rend


def millGal(km, l):
    rend = (km * .62137) / (l * .2996915)
    return rend

def litrosnecesarios(km,rendimiento):
    litros = km/rendimiento
    return litros

main()