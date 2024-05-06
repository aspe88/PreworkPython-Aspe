'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.'''

#1. Introduce el año
#2. Ejecuta ejercicio19.py
#3. Obten si el año es o no bisiesto.

def es_bisiesto(ano):
  if (ano %4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    return True
  return False

ano = int(input('Introduce un año para saber si es bisiesto: '))

if es_bisiesto(ano):
  print(f'El Año',ano,'es bisiesto')
else:
  print(f'El Año',ano,'no es bisiesto')