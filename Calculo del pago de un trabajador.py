#encoding: UTF-8
#Autor: Jesus Perea
#Cálculo del pago de un trabajador

def pagoSemanalNormal(horas,pagoxh):
    pagoSemanaN = horas * pagoxh
    return pagoSemanaN

def pagoSemanalExtras (horas, pagoxh):
    pagoSemanaE = horas * pagoxh
    return pagoSemanaE

def main():
    horasTrabajadas = int(input("Tecle el numero de horas trabajadas sin extras"))
    horasExtras = int(input("Teclea las horas extras trabajadas"))
    pagoPorHora = int(input("Teclea el pago por hora"))
    print("Horas normales", horasTrabajadas)
    print("Horas extras",horasExtras)
    print("Pago por hora",pagoPorHora)
    print("Pago semanal normal")
    psn = pagoSemanalNormal(horasTrabajadas,pagoPorHora)
    print (psn)
    print("Pago semanal extra")
    pse = pagoSemanalExtras(horasExtras,pagoPorHora)
    print(pse)
    
main()    