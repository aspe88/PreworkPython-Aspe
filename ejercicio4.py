'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario'''

# 1. Introduce la palabra a analizar entre las comillas del input palabra: ' palabra a analizar'
# 2. Ejecuta ejercicio4.py
# 3. Obtienes el número de volcaes de la palabra o frase

def contar_vocales(palabra):
    vocales = 'aeiouAEIOUáéióúÁÉÍÓÚ'
    a = 0
    for vocal in palabra:
        if vocal in vocales:
            a += 1
    return a

palabra = input('Introduce una palabra/frase: ')
numero_vocales = contar_vocales(palabra)
print(f'El número de vocales en la palabra es: {numero_vocales}')




