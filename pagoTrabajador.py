#Oscar Zuñiga Lara    A01654827

def pago(pagoH, horaN, horaE):
    pt = horaN * pagoH + horaE * pagoH * 1.5
    return pt

y = float(input("Inserte Horas normales:"))
z = float(input("Inserte Horas extras:"))
x = float(input("Inserte pago por Hora:"))


pagoTotal = pago(x , y , z)

print(pagoTotal)