'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

#1. Itroduce todos los números que quieras separados por comas entre los paréntesis
#2. Ejecuta ejercicio16.py
#3. Obten la cantidad de números pares e impares


lista = [1, 5, 7, 13, 22, 15, 26, 64, 34, 72, 52, -14]


a = 0
b = 0
for num in lista:
  if (num % 2) == 0:  
    a += 1
  else:  
    b += 1
print(f'En la lista hay',a,'números pares y',b,'numeros impares')

