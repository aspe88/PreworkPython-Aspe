'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

# 1. Introduce el importe del ticket.
# 2. Ejecuta ejercicio2.py
# 3. Obtienes total con propina incluida

price = float(input('Introduce precio en € '))
price_total = price*1.15


print(f'La factura total es de:', price_total, '€')