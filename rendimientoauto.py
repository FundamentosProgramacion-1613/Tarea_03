# encoding: UTF-8
#Blanca Flor Caldern Vazquez
#Autos
#Con esta función sabremos el rendimiento de tu auto
def rendirEnKmXL(Km,L):
    rendimiento=Km/L
    return rendimiento
#Con esta funcion sabremos el rendimiento de tu aunto en otras unidades
def rendirEnMiXGal(Mi,Gal):   
    rendimiento=((Mi/1.609344)/(Gal*0.264172051))
    return rendimiento
#Con esta funcion sabremos cuantos litros de necesitaras para cierto recorrido
def consumirEnLXKm(Km,Rendimiento):
    litros=Km/Rendimiento
    return litros

def main():
    KmRecorridos=float(input("Ingresa los Km recorridos"))
    LDeGasUtilizada=float(input("Ingresa los L de gas utilizados"))
    KmPorRecorrer=float(input("Ingresa los Km que quieres recorrer"))
    
    rendimiento1=rendirEnKmXL(KmRecorridos,LDeGasUtilizada)
    rendimiento2=rendirEnMiXGal(KmRecorridos,LDeGasUtilizada)
    consumo=consumirEnLXKm(KmPorRecorrer,rendimiento2)
    print("El rendimiento en Km/l es",rendimiento1)
    print("El rendimiento en mi/gal es",rendimiento2)
    print("Si recorres",KmPorRecorrer,"Km, necesitarás",consumo,"litros")
main()


