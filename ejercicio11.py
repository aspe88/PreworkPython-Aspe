'''Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.'''

#1.  Introduce tu año de nacimiento
#2. Ejecuta ejercicio11.py
#3. Obten tu edad.

ano = "1989"

from datetime import datetime
fecha_nacimiento = datetime.strptime(ano,"%Y")
edad = datetime.now().year - fecha_nacimiento.year

print("Tu edad es:", edad)