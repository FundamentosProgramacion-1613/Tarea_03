#encoding: utf-8
#autor: Allan Sánchez Iparrazar
#Rendimiento de autos

def calcularRendimientoKM_L(kilometros,gasolina):
    rendimiento = kilometros/gasolina
    return rendimiento
    
def calcularRendimientoMI_GAL(kilometro,gasolina):
    milla = kilometro/1.609344
    galon = gasolina*0.264172051
    
    rendimiento = milla/galon
    return rendimiento
    
def calcularRendimientoKM(kmARecorrer,rendimientoKM_L):
    rendimiento = kmARecorrer/rendimientoKM_L
    return rendimiento
    
    

def main():
    kilometros = int(input("Ingresa la cantidad de kilometros recorridos"))
    gasolina = int(input("ingresa la cantidad en litros de gasolina utilizada"))
    rendimientoKM_L = calcularRendimientoKM_L(kilometros,gasolina)
    rendimientoMI_GAL = calcularRendimientoMI_GAL(kilometros,gasolina)
    
    
    print("""Si recorre %.0f km con %.0f litros de gasolina,
El rendimiento en km/l es: %.2f
El rendimiento en mi/galon es: %.2f """%(kilometros,gasolina,rendimientoKM_L,rendimientoMI_GAL))
    kmARecorrer = int(input("¿Cuántos kilómetros vas a recorrer?"))
    
    rendimientoKM = calcularRendimientoKM(kmARecorrer,rendimientoKM_L)
    
    print("Para recorrer %.2f kilometros necesitas %.2f litros de gasolina"%(kmARecorrer,rendimientoKM))

main()