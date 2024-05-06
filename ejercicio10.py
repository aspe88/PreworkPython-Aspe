'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''

# 1. Introduce el numero del día de la semana
# 2. Ejecuta ejercicio10.py
# 3. Obten el día de la semana

n = int(input('Introduce el día de la semana del 1 al 7: '))

if n == 1:
  print('Lunes')
elif n == 2:
  print('Martes')
elif n == 3:
  print('Miércoles')
elif n == 4:
  print('Jueves')
elif n == 5:
  print('Viernes')
elif n == 6:
  print('Sábado')
elif n == 7:
  print('Domingo')
else :
  print("Error: Introduce un número de 1 al 7")
