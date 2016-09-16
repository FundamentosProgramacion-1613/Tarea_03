#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°3 de la tarea 3

def pagoSemanaNormal(horasNormales, pagoNormal):
    pagoSemanaN = horasNormales * pagoNormal
    return pagoSemanaN
    
def pagoSemanaExtra(horasNormales, pagoNormal):
    pagoSubtotal = horasNormales * pagoNormal
    pagoSemanaE = (pagoSubtotal * 50) /100 + pagoSubtotal
    return pagoSemanaE
    
def pagoTotal(totalNormales, totalExtras):
    totalSemana = totalNormales + totalExtras
    return totalSemana
   
def main():
    horasNormales = float(input("Horas Normales Trabajadas:"))
    horasExtra = float(input("Horas Extra Trabajadas:"))
    pagoNormal = float(input("Pago Normal:"))
    totalNormales = pagoSemanaNormal(horasNormales, pagoNormal)
    totalExtras = pagoSemanaExtra(horasNormales, pagoNormal)
    totalTotal = pagoTotal(totalNormales, totalExtras)
    print("Horas normales:", horasNormales)
    print("Horas extras:", horasExtra)
    print("Pago semanal total:$", format(totalNormales), sep="")
    print("Pago semanal extra:$", format(totalExtras), sep="")
    print("Pago semana total:$", format(totalTotal), sep="")
main()
    
    