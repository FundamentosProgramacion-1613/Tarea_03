#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 3

def calcularPagosemanal(horas,pago):
    h= horas * pago
    return h
    
def calcularPagosemanalextra(horasextras,pago):
    horasEx= float((horasextras * pago)*1.5)
    return horasEx
     
def main():
    horas= float(input("¿Cuantas horas trabajaste?"))
    horasextras= float(input("¿Con cuantas horas extras?"))
    pago= float(input("Pago por hora normal"))
    print ("Horas normales: ",horas)
    print ("Horas extreas: ",horasextras)
    print ("Pago por hora normal: $",pago)
    pagoSemanal= calcularPagosemanal(horas,pago)
    pagoSemanalEx= calcularPagosemanalextra(horasextras,pago)
    total= float(pagoSemanal + pagoSemanalEx)
    print ("Pago semanal normal: ",pagoSemanal)
    print ("Pago semanal extra: ",pagoSemanalEx)
    print ("Pago semanal total: ",total)
    
main()    