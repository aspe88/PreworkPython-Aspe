'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario'''

# 1. Introduce la palabra a analizar entre las comillas del input palabra: ' palabra a analizar'
# 2. Ejecuta ejercicio4.py
# 3. Obtienes el número de volcaes de la palabra o frase

palabra = 'holadasfasdgsbtreavgfreadgva'

vocales = 'a,e,i,o,u,A,E,I,O,U,á,é,i,ó,ú,Á,É,Í,Ó,Ú,'
a = 0
for vocal in palabra:
    if vocal in vocales:
        a += 1

print(f'El número de vocales en la palabra es:',a)
 


