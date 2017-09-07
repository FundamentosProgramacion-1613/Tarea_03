#Oscar Zuñiga Lara    A01654827

def main():
    hn = horasNormales()
    he = horasExtras()
    ph = pagoH()
    print(pagonormal(hn,ph))
    print(pagoExtra(he,ph))
    print(pagaTotal(hn, he, ph))

def horasNormales():
    horasN = float(input("Inserte Horas Normales"))
    return horasN

def horasExtras():
    horasE = float(input("Inserte Horas Extras"))
    return horasE

def pagonormal(horasN, costoH):
    pagoN = horasN * costoH
    return pagoN

def pagoExtra(horasE, costoH):
    pagoE = horasE * costoH * 1.5
    return pagoE

def pagoH():
    pagoh = float(input("Inserte pago por hora: "))
    return pagoh

def pagaTotal(pagoN, pagoE, pagoH):
    pagoT = pagoN * pagoH + pagoE * pagoH * 1.5
    return pagoT


main()