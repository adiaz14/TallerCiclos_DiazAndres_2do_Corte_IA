# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:58:03 2021

@author: Andrés Diaz
"""

import random

# Realice los procedimientos que den solución a los siguientes ejercicios.

# 1. El departamento de Seguridad de Transito de Barranquilla, desea saber de
# los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
# color. Conociendo el último digito de la placa de cada automóvil se puede
# determinar el color de la calcomanía utilizando la siguiente relación:

"""
--------------------------
|  Digito  |     Color   |
--------------------------
|  1 - 2   |   Amarillo  |
|  3 - 4   |   Rosa      |
|  5 - 6   |   Roja      |
|  7 - 8   |   Verde     |
|  9 - 0   |   Azul      |
--------------------------
"""

# Generar placa aleatoriamente (ejecutar el import random al inicio
# del archivo)


def generar_placa():
    placa = ''
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letras_placa = ''
    digitos_placa = ''
    for valor in range(3):
        letras_placa += letras[random.randint(0, 25)]
        digitos_placa += digitos[random.randint(0, 9)]
    placa = letras_placa + ' ' + digitos_placa
    return placa

# Generar cáculo de No de calcomanias


def conteo_calcomania(n_autos):
    if(n_autos > 0):
        ultimo_digito_placa = ""
        resultado = {'amarillo': 0, 'rosa': 0, 'roja': 0, 'verde': 0, 'azul':
                     0, 'número de Autos': 0, 'listado de placas': []}
        for valor in range(n_autos):
            placa = generar_placa()
            ultimo_digito_placa = int(placa[6:])
            if (ultimo_digito_placa > 0 and ultimo_digito_placa <= 2):
                resultado['amarillo'] += 1
            elif(ultimo_digito_placa >= 3 and ultimo_digito_placa <= 4):
                resultado['rosa'] += 1
            elif(ultimo_digito_placa >= 5 and ultimo_digito_placa <= 6):
                resultado['roja'] += 1
            elif(ultimo_digito_placa >= 7 and ultimo_digito_placa <= 8):
                resultado['verde'] += 1
            else:
                resultado['azul'] += 1
            resultado['número de Autos'] += 1
            resultado['listado de placas'].append(placa)
        print('\n---------- RESULTADOS DE LAS MUESTRAS ----------\n')
        for llave, valor in resultado.items():
            if(llave == 'número de Autos' or llave == 'listado de placas'):
                print(f'El {llave} es: {valor}')
            else:
                print(f'No de calcomanías de color {llave}: {valor}')
    else:
        print('\nLa cantidad de vehículos debe ser mayor a cero para la '
              'realización de calculos.\n')


print('\n----- DEPTO DE SEGURIDAD DE TRANSITO DE BARRANQUILLA (RESUMEN '
      'DE MOVILDIAD) -----\n')
n_autos = int(input('Ingrese cantidad de autos que ingresan a Barranquilla: '))
conteo_calcomania(n_autos)
