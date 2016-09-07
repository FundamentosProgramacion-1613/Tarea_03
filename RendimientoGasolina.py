#encoding: UTF-8
#Autor: Diego Perez AKA DiegoCodes
#Rendimiento De Autos

#Calcula Rendimiento por KM/L y milla por galon
def performance(km,l):
    kmlPerformance = km/l
    mgalPerformance = (km*1.609344)/(l*0.264172051)
    return kmlPerformance,mgalPerformance
   
def main():
    km = int(input("Kilometros Recorridos:"))
    l = int(input("Litros de Gasolina Utilizados:"))
    (kmlPerformance,mgalPerformance) = performance(km,l)
    print("Rendimiento en Km por Litro es de: %.2f " % kmlPerformance)
    print("Rendimiento en Milla por Galon es de: %.2f " % mgalPerformance)
    kmToTravel = int(input("Cuantos km recorrera?"))
    kmToTravelPerformance = kmToTravel/kmlPerformance
    print("Para recorrer",kmToTravel,"kms ,requiere de %.2f" % kmToTravelPerformance,"litros")
main()