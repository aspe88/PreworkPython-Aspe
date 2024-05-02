'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.'''

#1. Introduce el número en x
#2. Ejecuta ejercicio13.py
#3. Obten si el número es primo o no. Sino lo es obtiene también su primer divisor, distino de 1.

x = 1001

if x < 2:
  print('Los números negativos o menores de 2 no son primos.')
else:
  def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(f'', num,"No es primo.", n, "es su primer divisor diferente de 1.")
            return False
    print(f'',num,"es un número primo.")
    return True
  es_primo(x)
