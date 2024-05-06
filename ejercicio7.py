'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.'''

# 1. Introduce los 2 número a operar
# 2. Seleccióna la operación a realizar, escribiendo correctamente: suma, resta, multiplicación o división.
# 3. Ejecuta el ejercicio7.py
# 4. Obtener el resultado de la operación.

num1 = float(input('numero1: '))
num2 = float(input('numero2: '))
operador = str(input('símbolo: '))

resultado = 0

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2

print(f"El resultado de la",operador,'es', resultado)