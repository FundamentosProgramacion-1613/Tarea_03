#Encoding: UTF-8(
#Autor: Oswaldo Morales Rodriguez A01378566
#Conociendo las horas que trabaja calcular su pago

def main():
    horasn=int(input("Horas normales de trabajo"))
    horase=int(input("Horas extra de trabajo"))
    precio=int(input("Pago por hora"))
    pagoNormal=calcularPagoNormal(precio,horasn)
    pagoExtra=calcularPagoExtra(precio,horase)
    pagoTotal=pagoNormal+pagoExtra
    print("Horas normales",horasn)
    print("Horas extras",horase)
    print("Pago por hora",precio)
    print("Pago semanal normal",pagoNormal)
    print("Pago semanal extra",pagoExtra)
    print("Pago semanal Total",pagoTotal)
    
def calcularPagoNormal(precio,horasn):
    pagoNormal=precio*horasn
    return pagoNormal
    
def calcularPagoExtra(precio,horase):
    pago1=horase*precio
    pago2=pago1*.50
    pagoExtra=pago1+pago2
    return pagoExtra

main()