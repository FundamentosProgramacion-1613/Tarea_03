#Oscar Zuñiga Lara    A01654827

litrosG = float(input("¿Cuánto ha gastado?"))
kilometrosR = float(input("¿Cuánto ha recorrido?"))
                                #Pide los litros y kilometros
def kmL(km, l): #Define función que calcula el rendimiento en KM/L
    rendimiento = km/l
    return  rendimiento

def millasGalon(km, l): #Función que calcula el rendimiento en millas/galon
    rendimiento = (km/1.609344) / (l * 0.264172051 )
    return  rendimiento

print("El rendimiento es de: ", kmL(kilometrosR, litrosG), "Km/L.")
print("El rendimiento es de: ", millasGalon(kilometrosR, litrosG), "mi/galon.")