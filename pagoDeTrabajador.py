#encoding: utf-8
#autor: Allan Snchez Iparrazar
#Pago a trabajador

def pagoNormal(horasTrabajo,pagoPorHora):
    pagoNormal = horasTrabajo*pagoPorHora
    return pagoNormal

def pagoExtra(horasExtra,pagoPorHora):
    pagaExtra = (pagoPorHora + (pagoPorHora/2)) * horasExtra
    return pagaExtra


def main():
    horasTrabajo = int(input("Horas normales trabajadas"))
    horasExtra = int(input("Horas extra trabajadas"))
    pagoPorHora = float(input("Pago por hora normal"))
    
    pagaHorasNormales = pagoNormal(horasTrabajo,pagoPorHora)
    pagaHorasExtra = pagoExtra(horasExtra,pagoPorHora)
    pagaTotal = pagaHorasExtra + pagaHorasNormales
    
    print("Horas normales:",horasTrabajo)
    print("Horas extra:",horasExtra)
    print("Pago por hora: $%.2f"%pagoPorHora)
    print("Pago semanal normal: $%.2f"%pagaHorasNormales)
    print("Pago semanal extra: $%.2f"%pagaHorasExtra)
    print("Pago total semanal: $%.2f"%pagaTotal)

main()