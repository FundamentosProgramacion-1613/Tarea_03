#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran
#Problema 5

import math 
 
x= int(input("Dame el valor de x")) 
y= int(input("Dame el valor de y")) 
r= math.sqrt((x**2)+ (y**2)) 
angulo= math.atan2(x,y) 
grados= math.degrees(angulo) 
grados= 90-grados 
print ("La magnitud de r es:",r) 
print ("Angulo:", grados) 
