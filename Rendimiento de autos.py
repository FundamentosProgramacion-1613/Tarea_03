#Encoding: UTF-8(
#Autor: Oswaldo Morales Rodriguez A01378566
#Conociendo los litros que gasta en su reccorido dar su rendimiento y los litros de gasolina que necesitara para los kilometros

def main():
    kilometros=int(input("Kilometros recorridos"))
    litros=int(input("Litros gastados"))
    rendimiento1=calcularRendimiento1(kilometros,litros)
    rendimiento2=calcularRendimiento2(kilometros,litros)
    print("Si recorre",kilometros,"con",litros,"litros de gasolina")
    print("El rendimiento en km/l es:",rendimiento1)
    print("El rendimiento en mi/galon es:",rendimiento2)
    kilometrosRecorrer=int(input("Kilometros que va a recorrer"))
    gasolina=calcularGasolina(kilometrosRecorrer,rendimiento1)
    print("Para recorrer",kilometrosRecorrer,"kms., necesitas",gasolina,"litros")

def calcularRendimiento1(kilometros,litros):
    rendimiento1=kilometros/litros
    return rendimiento1
    
def calcularRendimiento2(kilometros,litros):
    milla=kilometros/1.609344
    galon=litros*0.264172051
    rendimiento2=milla/galon
    return rendimiento2

def calcularGasolina(kilometrosRecorrer,rendimiento1):
    gasolina=kilometrosRecorrer/rendimiento1
    return gasolina
main()
    