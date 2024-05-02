'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.'''

#1. Introduce el año
#2. Ejecuta ejercicio19.py
#3. Obten si el año es o no bisiesto.

year = 2025

if year %4 != 0:
  print(f'El Año',year,'no es bisiesto')
else:
  print(f'El Año',year,'es bisiesto')