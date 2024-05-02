'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario'''

#1. Introduce todos los numeros que quieras entre los corchetes, separados por comas
#2. Ejecuta ejercicio20.py
#3. Obten el resultado de la suma


numeros =[10,1,1,1,1,1,1,1,1,1,1,1]

suma = 0
for numero in numeros:
  suma += numero
print(f'La suma total es',suma)