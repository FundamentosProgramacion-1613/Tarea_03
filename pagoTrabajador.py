#Oscar Zuñiga Lara    A01654827

def pago(pagoH, horaN, horaE):   #Funcion que calcula el pago
    pt = horaN * pagoH + horaE * pagoH * 1.5
    return pt

y = float(input("Inserte Horas normales:"))
z = float(input("Inserte Horas extras:"))
x = float(input("Inserte pago por Hora:"))

                                        #Solicita las horas y el pago

pagoTotal = pago(x , y , z)
                                #Invoca función pago
print(pagoTotal)    #Imprime el pago total