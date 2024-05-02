'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''

# 1. Introduce tu peso y altura
# 2. Ejecuta ejercicio8.py
# 3. Obtienes un IMC Índice de masa corporal

peso = 75
altura = 1.75

imc = peso/altura**2
print(f'Tu índice de masa corporal es de:',imc)
if imc < 18.5 :
  print('Hay que ir a casa de la abuela')
elif imc > 25:
  print('Hay que dejar de comer bollos')
else :
  print('Estás en tu prime')



