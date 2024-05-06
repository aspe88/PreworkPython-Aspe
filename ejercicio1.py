'''Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit'''

# 1. Introduce la temperatura en Celsis en Cº
# 2. Ejecuta ejercicio1.py
# 3. Obtiene temperatura en Fº


def conversor(C):
  return C * (9/5) + 32

C = float(input('Introduce la temperatura en Cº: '))
F = conversor(C)
print(f'La temperatura en Fº es:',F)