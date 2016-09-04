#encoding: UTF-8
#Karla Valeria Alcantara Duarte A01373164
#Calcular pago de un trabajador.

def calcularPagoNormal(horaNormal,pagoHora): #Calcula pago por las horas normales trabajadas
    pagoNor = horaNormal*pagoHora
    return pagoNor
    
def calcularPagoExtra(horaExtra,pagoHora): #Calcula pago por las horas extra trabajadas 
    pagoHoraExtra = pagoHora+(pagoHora*0.50)
    pagoEx = pagoHoraExtra*horaExtra
    return pagoEx
    
def main():
    horaNormal = int(input("Horas normales trabajadas"))
    horaExtra = int(input("Horas extra trabajadas"))
    pagoHora = int(input("Pago por hora normal"))
    pago1 = calcularPagoNormal(horaNormal,pagoHora)
    pago2 = calcularPagoExtra(horaExtra,pagoHora)
    pagoTotal = pago1+pago2
    print("Horas normales trabajadas:",horaNormal)
    print("Horas extra trabajadas:",horaExtra)
    print("Pago por hora:",pagoHora)
    print("Pago semanal normal:",pago1)
    print("Pago semanal extra:",pago2)
    print("Pago total:",pagoTotal)
    
main()

    
