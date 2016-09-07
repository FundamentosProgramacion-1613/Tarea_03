#encoding:UTF-8
#Ma Fernanda Rodriguez Hrdz
#escribir un programam que calcule el pago normal y el pago extra de un trabajador

def pagoNormal(normal,pago):
    pagoNormal = normal * pago
    return pagoNormal

def pagoExtra(extra,pago):
    # aplicando el 50% mas 
    pagoHorasExtra = (pago * .5) + pago
    pagoExtra = pagoHorasExtra * extra
    return pagoExtra  


def main():
    normal = int(input("horas normales trabajadas"))
    extra = int(input("horas extras trabajadas"))
    pago = float(input("pago normal por hora"))
    pagoNormal(normal,pago)
    pagoExtra(extra,pago)
    
    print(
    "horas normales",normal,
    "\nhoras extras",extra,
    "\npago por hora",pago,
    "\npago semanal normal",pagoNormal(normal,pago),
    "\npago semanal extra",pagoExtra(extra,pago),
   
    )

main()