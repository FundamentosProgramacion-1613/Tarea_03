#encoding: UTF-8
#Karla Valeria Alcantara Duarte A01373164
#Calcular rendimiento de un automovil.

def calcularRendimientoKmL(kilometros, litros): #Calcula rendimiento de auto en kilometros/litros
    rendimiento = kilometros/litros
    return rendimiento
    
def convertirKm(kilometros): #Convierte de kilometros a millas
    millas = kilometros/1.609
    return millas
    
def convertirL(litros): #Convierte de litros a galones
    galones = litros*0.2641
    return galones
    
def calcularRendimientoMiGa(millas,galones): #Calcua rendimiento del auto en millas/galon
    rendimiento = millas/galones
    return rendimiento
    
def calcularGasolina(kilometros2):
    gasolina = kilometros2/15.2 #Basandose en un automovil que consume 15.2 km/l calcular la gasolina necesaria de acuerdo a los kilometros a recorrer
    return gasolina
    
def main():
    kilometros = int(input("Kilometros recorridos"))
    litros = int(input("Litros de gasolina usados"))
    rendimiento1 = calcularRendimientoKmL(kilometros,litros)
    millas = convertirKm(kilometros)
    galones = convertirL(litros)
    rendimiento2 = calcularRendimientoMiGa(millas,galones)
    
    print ("Si se recorren",kilometros,"km con",litros,"de gasolina")
    print("El rendimiento en Km/l es",("%.02f")%(rendimiento1))
    print("El rendimiento en mi/g es",("%.02f")%(rendimiento2))
    
    kilometros2 = int(input("¿Cuantos kilometros vas a recorrer?"))
    gasolina = calcularGasolina(kilometros2)
    
    print("Necesitas:",("%.02f")%(gasolina),"litros de gasolina para recorrer",kilometros2,"kilometros")
    
main()