#encoding:UTF-8
#Autor: Carlos E. Carbajal Nogus
#Descripcion: programa que calcula los pagos de un trabajador
#Inicio
def calcularPago_normal(horasNormales,pagoHora): #Función que calcula los pagos por horas de trabajo normales
    res1= horasNormales*pagoHora
    return res1

def calcularPago_extra(horasExtra,pagoHora): #Función que calcula los pagos por horas extras
    res2=horasExtra*(pagoHora*1.5)
    return res2

def main(): #Función principal
    hn=int(input("¿Cuántas horas normales trabajaste?"))
    he=int(input("¿Cuántas horas extra trabajaste?"))
    pg=int(input("¿Cuál es tu paga normal?"))
    psn=calcularPago_normal(hn,pg)
    pse=calcularPago_extra(he,pg)
    res = psn + pse
    print("""    Tu pago semanal por horas normales es: %.2f
    Tu pago semanal por horas extras es: %.2f
    Tu pago total semanal es: %.2f""" %(psn,pse,res))

main()
#Fin