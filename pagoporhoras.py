# encoding: UTF-8
#Blanca Flor Caldern Vazquez
#Pago de un trabajador

#Con esta funcion obtendremos el pago semanal de horas laboradas  normales
def pagarSemanalNormal(horasNormales,cantidadApagar):
    pago=horasNormales+cantidadApagar
    return pago
#Con esta funcion obtendremos el pago semanal de horas extra
def pagarSemanalExtra(horasExtra,cantidadApagar):
    pago=horasExtra*(cantidadApagar*1.5)
    return pago
#Con esta funcion obtendremos el pago semanal de horas totales
def pagarSemanalTotal(pagoExtra,pagoNormal):
    pago=pagoExtra+pagoNormal
    return pago
def main():
    horasNormales=int(input("Introduce horas normales trabajadas en la semana"))
    horasExtra=int(input("Inttroduce horas extra trabajadas en la semana"))
    unidadDePago=70
    PagoSemanalNormal=pagarSemanalNormal(horasNormales,unidadDePago)
    PagoSemanalExtra=pagarSemanalExtra(horasExtra,unidadDePago)
    PagoSemanalTotal=pagarSemanalTotal(PagoSemanalExtra,PagoSemanalNormal)
    
    print("Pago por horas laborales",PagoSemanalNormal)
    print("Pago por horas laborales extra",PagoSemanalExtra)
    print("Pago total por laborar",PagoSemanalTotal)
main()