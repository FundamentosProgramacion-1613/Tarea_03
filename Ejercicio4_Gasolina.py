# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Cálculo del rendimiento de un carro 

# Función que convierte kilómetros sobre litro en millas sobre galón
def convertirRendimiento(rendimiento):
    conversion = rendimiento/(1.609344*0.264172051)
    return conversion
    
def main():
    kilometros = int(input("Kilómetros recorridos"))
    litros = int(input("Litros de gasolina utilizados"))
    rendimientoKmL = kilometros/litros
    rendimientoMiG = convertirRendimiento(rendimientoKmL)
    print("Si recorre", kilometros, "km con", litros, "litros de gasolina,")
    print("El rendimiento en km/l es: ", format(rendimientoKmL, ".2f"))
    print("El rendimiento en mi/galón es: ", format(rendimientoMiG, ".2f"))
    kilometros =  int(input("¿Cuántos kilometros vas a recorrer?"))
    litros = kilometros/rendimientoKmL
    print("Para recorrer", kilometros, "kms., necesitas", format(litros, ".2f"), "litros")
main()