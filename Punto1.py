# -*- coding: utf-8 -*-

#Una Institución educativa ha recibido una donación especial que será 
#epartida entre las carreras de Telecomunicaciones, Sistemas, 
#Administración y Contabilidad de la siguiente forma:
#a. Telecomunicaciones 10% del valor dado a sistemas
#b. Sistemas: 25% del valor dado a Administración
#c. Administración: 35% del valor de la donación
#d. Contabilidad: lo que resta de la donación

valordonado = int(input("Valor total donado"))
vadministracion = valordonado * 0.35
vsistemas = vadministracion * 0.25
vtelecomunicaciones = vsistemas * 0.1
vcontabilidad = valordonado - vtelecomunicaciones - vsistemas - vadministracion

print(f"EL valor total donado: {valordonado}")
print(f"Para el area de Telecomunicaciones = {vtelecomunicaciones} ")
print(f"Para el area de sistemas = {vsistemas} ")
print(f"Para el area de administracion = {vadministracion} ")
print(f"Para el area de contabilidad = {vcontabilidad} ")


