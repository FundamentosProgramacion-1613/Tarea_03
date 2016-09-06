#encoding: UTF-8
#Autor: Jesus Perea 
#Rendimiento de autos

def calcularKiloEntreLitros (kilo,litros):
    KML = kilo / litros
    return KML

def calcularMillasEntreGalones (millas,galones):
    MillasGa = millas / galones
    return MillasGa
    
def calcularLitrosNecesarios (KM,rendimiento):
    Litros =  KM / rendimiento     
    return Litros

def main ():
    numeroDeKM = int(input("Teclea el numero de kilometros recorridos"))
    litrosDeGasolina = int(input("Teclea el numero de litros que utilizaste"))
    
    ckl = calcularKiloEntreLitros(numeroDeKM, litrosDeGasolina)
    
    Galones = litrosDeGasolina * 0.264172051
    Millas = numeroDeKM / 1.609344
    
    cmg = calcularMillasEntreGalones (Millas,Galones)
    
    KilometrosDeViaje = int(input("Teclea el número de kilometros que vas a recorrer"))
    cLn = calcularLitrosNecesarios(KilometrosDeViaje,calcularKiloEntreLitros(numeroDeKM, litrosDeGasolina))    
    
    print("Si recorre",numeroDeKM,"con",litrosDeGasolina)
    print("El rendimiento en km/l es:", ckl)
    print("El rendimiento en mi/gal es:",cmg)
    print("Para recorrer",KilometrosDeViaje,", necesitas",cLn,"litros")
    
main()