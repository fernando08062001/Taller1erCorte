# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:30:36 2022

@author: ffiorill
"""

redes = int(input("Alumnos en Redes: "))
cont = int(input("Alumnos en Contabilidad: "))
diseño = int(input("Alumnos en Diseño: "))

total = redes + cont + diseño

predes = redes/total*100
pcont = cont/total*100
pdiseño = diseño/total*100

print(f"El total de estudiantes seria: {total}")
print(f"En redes hay un: {predes}% con respecto al total")
print(f"En contabilidad hay un: {pcont}% con respecto al total")
print(f"En diseño hay un: {pdiseño}% con respecto al total")
