#encoding: UTF-8
# Autor: Adrin E. Tllez Lpez
#

def calcularNormal(hnt, pgn):
    HorasNormal = hnt * pgn
    return HorasNormal

def calcularExtra(het, pgn):
    extra = (het * pgn) * 0.5
    HorasExtra = (het * pgn) + extra
    return HorasExtra


def main():
    hnt = int(input("Horas normales trabajadas"))
    het = int(input("Horas normales trabajadas"))
    pgn = int(input("Horas normales trabajadas"))
    psn = calcularNormal(hnt, pgn)
    pse = calcularExtra(het, pgn)
    pst = psn + pse
    print ("Horas normales:", hnt)
    print ("Horas extras:", het)
    print ("Pago por hora:", pgn)
    print ("Pago semanal normal:", psn)
    print ("Pago semanal extra:", pse)
    print ("Pago semanal total:", pst)
    
main()