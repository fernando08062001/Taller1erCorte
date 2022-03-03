# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:18:49 2022

@author: ffiorill
"""
taller1 = int(input("Nota del taller 1: "))
taller2 = int(input("Nota del taller 2: "))
taller3 = int(input("Nota del taller 3: "))
examen = int(input("Nota del examen en clase: "))
proyecto = int(input("Nota del proyecto: "))

promtalleres = (taller1 + taller2 + taller3) / 3
porcnota = (promtalleres*0.5)+(examen*0.3)+(proyecto*0.2)

print(f"Tu nota final es: {porcnota}") 
