'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''

#1. Introduce los minutos en el campo x
#2. Ejecuta ejercicio15.py
#3. Obten el resultado en horas y minutos

x = 145

y = int(x/60)
f = x-(y*60)
print(f'Los minutos indicados son',y,'horas y',f,'minutos')