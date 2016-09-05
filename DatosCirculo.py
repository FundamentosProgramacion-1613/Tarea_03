
#encoding: UTF-8

#Autor: José Javier Rodríguez Mota
#Descripción: Programa que toma el radio de un círculo y te da el diámetro, la longitud de circunferencia y el área

#Importamos pi
from math import pi
#Inicio
#Definimos función para calcular diámetro
def calcularDiametro(r):
    d=2*r
    return d
#Definimos función para calcular longitud
def calcularLongitud(r):
    l=calcularDiametro(r)*pi
    return l
#Definimos función para calcular área
def calcularArea(r):
    a=pi*r**2
    return a
#Definimos Main
def main():
#Pedimos el radio
    r=float(input("Escribe el radio del círculo"))
    d=calcularDiametro(r)
    l=calcularLongitud(r)
    a=calcularArea(r)
    print("""Círculo con radio: %.1f
Diámetro: %.2f
Circunferencia: %.2f
Área: %.2f """%(r,d,l,a))

#Ejecutamos el programa
main()
#Fin