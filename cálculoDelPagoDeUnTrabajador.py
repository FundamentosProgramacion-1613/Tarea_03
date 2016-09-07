#encoding: UTF-8

# Autor: Marina Itzel Haro Hernndez, A01373471
# Calcula el pago de un trabajador



def calcularPagoNormal(pagoPorHora, horasNormales):
    pagoNormal = horasNormales * pagoPorHora
    return pagoNormal

def calcularPagoExtra(pagoPorHora, horasExtras):
    pagoExtra = horasExtras * ((pagoPorHora*.5)+pagoPorHora)
    return pagoExtra
 
    
def main():
    horasNormales = int(input("Horas normales trabajadas"))
    horasExtras = int(input("Horas extras trabajadas"))
    pagoPorHora = int(input("Pago por hora normal"))
    pagoNormal = calcularPagoNormal(pagoPorHora, horasNormales)
    pagoExtra = calcularPagoExtra(pagoPorHora, horasExtras)
    pagoSemanalNormal = horasNormales * pagoPorHora
    pagoSemanalExtra = pagoExtra
    pagoSemanalTotal = pagoSemanalNormal + pagoSemanalExtra
    print("Horas normales:", horasNormales)
    print("Horas extras:", horasExtras)
    print("Pago por hora: $%.2f" % (pagoPorHora))
    print("Pago semanal normal: $%.2f" % (pagoSemanalNormal))
    print("Pago semanal extra: $%.2f" % (pagoSemanalExtra))
    print("Pago semanal total: $%.2f" % (pagoSemanalTotal))
    
main()
    