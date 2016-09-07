#encoding:UTF-8
#Autor:Lenin Silva Gutiérrez, A01373214
#Regresa datos de un círcula para un radio dado

from math import pi

#obtiene el diámetro del círculo y regresa su valor
def calcularDiametro(radio):
    diametro=2*radio
    return diametro

#obtiene la circunferencia del círculo y regresa su valor        
def calcularCircunferencia(radio):
    circunferencia=2*pi*radio
    return circunferencia

#obtiene el área del círculo y regresa su valor        
def calcularArea(radio):
    area=(pi*radio**2)
    return area

def main():
    radio=float(input("Radio del círculo"))
    diametro=calcularDiametro(radio)
    circunferencia=calcularCircunferencia(radio)
    area=calcularArea(radio)
    print ("Círculo con radio: %.2f"%(radio))
    print ("Diámetro: %.2f"%(diametro))
    print ("Circunferencia: %.2f"%(circunferencia))
    print ("Area: %.2f"%(area))
    
main()