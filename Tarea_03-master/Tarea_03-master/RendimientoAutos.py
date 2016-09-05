#encoding: UTF-8
#Autor: Aldo Fuentes - A01373294
#Calcular rendimiento de Auto

def rendimientokml(km, l):
    rendimiento = km / l
    return rendimiento
    
def conversion(rendimiento):
    conversion = rendimiento * 2.352
    return conversion
    
def litros(km, rendimiento):
    litros = km / rendimiento
    return litros
    
def main():
    kmRecorridos = int(input("Kilometros recorridos"))
    lUtilizados = int(input("Litros de gasolina utilizados"))
    
    r = rendimientokml(kmRecorridos, lUtilizados)
    c = conversion(r)
    
    print("Si recorre",kmRecorridos,"km con",lUtilizados,"litros de gasolina,")
    print("El rendimiento en km/l es: ", "%.2f" % r)
    print("El rendimiento en mi/galon es : ", "%.2f" % c)
    
    km = int(input("¿Cuantos kilometros vas a recorrer?"))
    
    l = litros(km, r)
    
    print("Para recorrer",km,"kms., necesitas","%.2f" % l,"litros")
    
main()
    

     