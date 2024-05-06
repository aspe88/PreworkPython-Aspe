'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

#1. Itroduce todos los números que quieras separados por comas entre los paréntesis
#2. Ejecuta ejercicio16.py
#3. Obten la cantidad de números pares e impares

def contar_par_impar(lista):
  pares = 0
  impares = 0
  for num in lista:
    if (num % 2) == 0:  
      pares += 1
    else:  
      impares += 1
  return pares, impares

numeros = list(map(int,input('Introduce la lista de numeros separados por espacios: ').split()))
pares, impares = contar_par_impar(numeros)
print(f'En la lista hay',pares,'números pares y',impares,'numeros impares')

