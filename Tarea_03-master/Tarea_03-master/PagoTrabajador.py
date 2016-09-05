#encoding: UTF-8
#Autor: Aldo Fuentes - A01373294
#Calcular pago de un trabajador

def pagoNormal(horasNormales, pagoPorHora):
    pagoNormal = horasNormales * pagoPorHora
    return pagoNormal
    
def pagoExtra(horasExtra, pagoPorHora):
    pagoExtra = horasExtra * pagoPorHora + horasExtra * pagoPorHora * .5
    return pagoExtra
    
def pagoTotal(pagoNormal, pagoExtra):
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal
    
def main():
    hN = int(input("Horas Normales Trabajadas"))
    hE = int(input("Horas extra trabajadas"))
    pH = float(input("Pago por hora normal"))
    
    pN = pagoNormal(hN, pH)
    pE = pagoExtra(hE,pH)
    pT = pagoTotal(pN, pE)
    
    print("Horas normales: ", hN)
    print("Horas extras: ", hE)
    print("Pago por hora: $", "%.2f" % pH)
    print("Pago semanal normal: $", "%.2f" % pN)
    print("Pago semanal extra: $", "%.2f" % pE)
    print("Pago semanal total: $", "%.2f" % pT)
    
main()