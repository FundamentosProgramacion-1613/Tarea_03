
#encoding: UTF-8

#Autor: José Javier Rodríguez Mota
#Descripción: Programa para calcular el precio de renta de películas

#Inicio
#Definimos nuestra función para calcular la renta
def calcularRenta(nE,nN):
#Calculamos el precio por estrenos
    pE=nE*45
#Calculamos el precio por normales
    pN=nN*27
#Damos el total
    pT=pE+pN
    return pT
#Definimos la función Main
def main():
#Pedimos los valores de entrada
    e=int(input("Películas de estreno"))
    n=int(input("Películas normales"))
#Calculamos el precio    
    t=calcularRenta(e,n)
#Imprimimos resultados
    print("""Películas de estreno rentadas: %d
Películas normales rentadas: %d
Total a pagar: $%.2f"""%(e,n,t))

#Ejecutamos el código
main()
#Fin   