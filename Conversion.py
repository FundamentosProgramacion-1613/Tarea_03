#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 4

milla= 1.609344
litro= 0.264172051

def calcularMilla(km):
    m= float(km/milla)
    return m
    
def calcularGalon(l):
    g= float(l*litro)
    return g 

def calcularLitros(v,l,km):
    f= float((v * l)/km)
    return f
        
def main():
    km= float(input("Kilometros recorridos"))
    l= float(input("Litros de gasolina ocupados"))
    t= float(km/l)
    print ("Si recorre ",km,"km con ",l,"litros de gasolina,")
    print ("El rendimiento de km/l es:",t)
    converM= calcularMilla(km)
    converG= calcularGalon(l)
    converTotal= float(converM/converG)
    print ("El rendimiento de mi/galon es:",converTotal)
    v= float(input("¿Cuanto km vas a recorrer?"))
    Litrostot= calcularLitros(v,l,km)
    print ("Para recorrer",v,"km necesitas",Litrostot,"litros")
    
    
main()       