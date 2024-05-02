'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

numbers= list(range(100))
i = 0
number = 0
while number < 100:
  number +=1
  if number%2 == 0:
    i +=1

print(i)




