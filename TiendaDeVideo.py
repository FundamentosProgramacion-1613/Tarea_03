#encoding: UTF-8
#Autor: Diego Perez AKA DiegoCodes
#Calculador de Precio por Peliculas

#Suma el costo de las peliculas multiplicandolas por su precio correspondiente
def rentCost(new,normal):
    total = (45*new)+(27*normal)
    return total
    
def main():
    new = int(input("Ingrese cantidad de peliculas estreno rentadas"))
    normal = int(input("Ingrese cantidad de peliculas normales rentadas"))
    total = rentCost(new,normal)
    print("Peliculas de estreno rentadas:",new)
    print("Peliculas normales rentadas:",normal)
    print("Total a Pagar: $",total)
main()