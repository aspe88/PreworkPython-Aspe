'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.'''

# 1. Introduce en la longitud en en primero campo, y el acncho en el segundo campo en cm
# 2. Ejecuta el ejercicio12.py
# 3. Obten el área en cm2 (si introuces otra undiades, obtendrás esas unidades al cuadrado)

l = float(input('Introduce el largo en cm: '))
a = float(input('Introduce el ancho en cm: '))

s = l*a
print(f'El area del rectángulo es de:',s,'cm2')
