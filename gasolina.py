#encoding:UTF-8
#Ma Fernanda Rodriguez Hrdz
#escribir un programam que reciba la cantidad de gasolina usada y los kilometros recorridos por un auto e imprime el rendimiento del auto y la cantidad de gasolina que necesitara para su proximo viaje

def rendimiento(kilometros,gasolina):
    #calculando el rendimiento en km/l
    a = kiometros / gasolina
    #calculando el rendimiento en millas/galon
    b = (kilometros*1.60)/(gasolina*0.26)
    return a
    return b
    def gasolinaFaltante():
        kmporrecorrer = float(input("cuantos kilometros vas a recorrer?"))
        #con el rendimiento calculamos la gasolina que necesita para recorrer x km
        litros_necesitados = a / kmporrecorrer 
        print ("para recorrer",kmporrecorrer,"km necesitas",litros_necesitados,"l de gasolina")
    

def main():
    kilometros = float(input("kilometros recorridos"))
    gasolina = float((input("litros de gasolina usada"))
    rendimiento(kilometros,gasolina)
     print (
    "si recorre",kilometros,"km con",gasolina,"de gasolina,"
    "\nel rendimiento en km/l es:",a,
    "\nel rendimiento en millas/galon es:",b
    )
    
main()