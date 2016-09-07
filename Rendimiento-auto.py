#encoding:UTF-8
#Autor:Lenin Silva Gutirrez, A01373214
#Calcula el rendimiento de un automóvil

#calcula el rendimiento en km por litro de gasolina
def calcularRendimientoKm(km, litro):
    rendimiento=km/litro
    return rendimiento

#calcula el rendimiento en millas por litro de gasolina        
def calcularRendimientoMillas(km, litro):
    millas=km/1.60934
    galon=litro*0.264172051
    rendimiento=millas/galon
    return rendimiento
    
#calcula los litros que se requieren para recorrer cierta distancia de acuerdo con el rendimiento obtenido    
def calcularLitrosNecesarios(km_recorrer, rendimiento):
    litros_necesarios=km_recorrer/rendimiento
    return litros_necesarios
    
def main():
    km=int(input("Kilómetros recorridos"))
    litros=int(input("Litros de gasolina utilizados"))
    rendimiento_km=calcularRendimientoKm(km, litros)
    rendimiento_millas=calcularRendimientoMillas(km, litros)
    print ("Si recorre %d km con %d litros de gasoilna,"%(km, litros))
    print ("El rendimiento en km/l es de: %.2f"%(rendimiento_km))
    print ("El rendimiento en mi/galon es de: %.2f"%(rendimiento_millas))
    km_recorrer=int(input("¿Cuántos kilómetros vas a recorrer?"))
    litros_necesarios=calcularLitrosNecesarios(km_recorrer, rendimiento_km)
    print ("Para recorrer %d kilómetros, necesitas %.2f litros"%(km_recorrer, litros_necesarios))
    
main()
    
    
    