'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''

#1. Introduce la frase de la que quieras contar las palabras entre las comillas
#2. Ejecuta ejercicio18.py
#3. Obten el número de palabras de la frase


frase = str(input('Introduce tu frase: '))

palabras = frase.split()
i = 0
for palabra in palabras:
    i+=1
print(f'La frase contiene',i,'palabras')
