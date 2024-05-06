'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

numbers= list(range(100))

number = 0
ammount = 0
while number < 100:
  number +=1
  if number%2 == 0:
    ammount = ammount + number


print(f'La suma de todos los números del 1 al 100 es: ',ammount)




