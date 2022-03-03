# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:06:28 2022

@author: ffiorill
"""

vend = int(input("Sueldo base del vendedor al mes: "))
ventas = int(input("Total de ventas realizadas por el vendedor: "))

porcventas = ventas * 0.15

pagomes = vend + porcventas

print(f"EL total  ganado por el vendedor en el mes de febrero seria: {pagomes}")