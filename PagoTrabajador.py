
#encoding: UTF-8

#Autor: José Javier Rodríguez Mota
#Descripción: Calcula el pago de un trabajador

#Inicio
#Definimos el código para calcular el total de pago
def calcularHorasn(hn,phn):
#Calculamos el pago por hora normal
    pn=hn*phn
    return pn
def calcularHorase(he,phn):
#Calculamos el pago por hora extra
    pe=he*phn*1.5
    return pe
#Definimos main
def main():
#Pedimos los valores de entrada
    hn=int(input("Horas normales trabajadas"))
    he=int(input("Horas extras trabajadas"))
    phn=float(input("Pago por hora normal"))
#Iniciamos cálculos
    pn=calcularHorasn(hn,phn)
    pe=calcularHorase(he,phn)
    t=pn+pe
#Imprimimos resultados
    print("""Horas normales: %d
Horas extras: %d
Pago por hora: $%.2f
Pago semanal normal: $%.2f
Pago semanal extra: $%.2f
Pago semanal total: $%.2f"""%(hn,he,phn,pn,pe,t))

#Iniciamos el código
main()
#Fin