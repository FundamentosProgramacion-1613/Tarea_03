
#encoding: UTF-8

#Autor: José Javier Rodríguez Mota
#Descripción: Calcula el rendimiento de un auto en km/l y millas/galón

#Inicio
#Definimos el código para calcular el rendimiento en km/l
def calcularRendimiento(k,l):
#Calculamos el pago por hora normal
    r=k/l
    return r
def transformarMG(r):
#Transformamos el rendimiento
    r2=r/1.609344/0.264172051
    return r2
#Calculamos la gasolina necesaria
def calcularGasolina(km,r):
    g=km/r
    return g
#Definimos main
def main():
    #Pedimos los valores de entrada iniciales
    k=float(input("Kilómetros recooridos"))
    l=float(input("Litros de gasolina utilizados"))
    #Iniciamos cálculos
    r=calcularRendimiento(k,l)
    r2=transformarMG(r)
    #Imprimimos resultados
    print("""Si recorre %d km con %d litros de gasolina,
    El rendimiento en km/l es: %.2f
    El rendimiento en mi/galón es: %.2f"""%(k,l,r,r2))
    #Solicitamos el valor adicional    
    km=float(input("¿Cuántos kilómetros vas a recorrer?"))
    #Hacemos cálculos
    g=calcularGasolina(km,r)    
    #Imprimimos el valor final
    print("Para recorrer %d km, necesitas %.2f litros de gasolina"%(km,g))    

#Iniciamos el código    
main()
#Fin