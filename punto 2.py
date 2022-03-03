# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:49:35 2022

@author: ffiorill
"""

#Haga un programa en Python que permita ingresar el dinero invertido por 
#tres personas para formar una empresa. Cada una de ellas invierte una 
#cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto 
#al total de la inversión.


per1 = int(input("Valor invertido por el #1"))
per2 = int(input("Valor invertido por el #2"))
per3 = int(input("Valor invertido por el #3"))

total = per1 + per2 + per3

porc1 = per1/total*100
porc2 = per2/total*100
porc3 = per3/total*100

print(f"El porcentaje de inversion que tiene el primer individuo es: {porc1}%")
print(f"El porcentaje de inversion que tiene el segundo individuo es: {porc2}%")
print(f"El porcentaje de inversion que tiene el tercer individuo es: {porc3}%")