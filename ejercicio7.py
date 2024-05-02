'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.'''

# 1. Introduce los 2 número a operar
# 2. Seleccióna la operación a realizar, escribiendo correctamente: suma, resta, multiplicación o división.
# 3. Ejecuta el ejercicio7.py
# 4. Obtener el resultado de la operación.


num1=10
num2=5
operador = 'suma'


resultado = 0

if operador == 'suma':
    resultado = num1 + num2
elif operador == 'resta':
    resultado = num1 - num2
elif operador == 'multiplicación':
    resultado = num1 * num2
elif operador == 'división':
    resultado = num1 / num2

print(f"El resultado de la",operador,'es', resultado)