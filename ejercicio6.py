'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)'''

# 1. Introduce la palabra a analizar en palabra
# 2. Ejecuta ejercicio6.py
# 3. Te indica si la plabra es o no un palíndromo

palabra = str(input('Introduce una palabra y comprueba si es un palíndromo: '))
if palabra == palabra[::-1]:
  print(f'la palabra',palabra,'es un palíndromo')
else:
  print(f'la palabra',palabra,'no es palidromo')