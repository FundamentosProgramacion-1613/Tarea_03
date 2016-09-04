# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Cálculo del sueldo de un trabajador

# Función que calcula el pago por las horas normales trabajadas
def calcularPagoNormal(horas, pago):
    total = horas*pago
    return total
    
# Función que calcula el pago por las horas extras trabajadas
def calcularPagoExtra(horas, pago):
    total = horas*pago*1.5
    return total

def main():
    horasNormales = int(input("Horas normales trabajadas"))
    horasExtras = int(input("Horas extras trabajadas"))
    pagoHora = float(input("Pago por hora normal"))
    pagoNormal = calcularPagoNormal(horasNormales, pagoHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoHora)
    pagoTotal = pagoNormal + pagoExtra
    print("Horas normales: ", horasNormales)
    print("Horas extras: ", horasExtras)
    print("Pago por hora: $", format(pagoHora, ".2f"), sep="")
    print("Pago semanal normal: $", format(pagoNormal, ".2f"), sep="")
    print("Pago semanal extra: $", format(pagoExtra, ".2f"), sep="")
    print("Pago semanal total: $", format(pagoTotal, ".2f"), sep="")
main()