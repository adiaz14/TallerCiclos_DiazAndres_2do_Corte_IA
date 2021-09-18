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

# 2. Un Zoólogo pretende determinar el porcentaje de animales que hay en las
# siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
# de 3 o mas años. El zoológico todavía no está seguro del animal que va
# estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
# si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
# 40.

# Supuestos: Para el número random se ha tenido en cuenta una edad entre 1 y 56
# debido a:
# Edad máx media de elefantes: 56 años
# Edad máx media de jirafas: 25 años
# Edad máx media de chimpancés: 40 años

# Generar cálculo de % de edad de animales


def porcentaje_edades_animales(animal=''):
    animal = animal.lower()
    if(animal != ''):
        acum_rango_uno = 0
        acum_rango_dos = 0
        acum_rango_tres = 0
        participacion_uno = 0
        participacion_dos = 0
        participacion_tres = 0
        contador_uno = 0
        contador_dos = 0
        contador_tres = 0
        contador = 0
        suma_edades = 0
        edades = []
        if(animal == 'elefantes'):
            no_muestras = 20
        elif(animal == 'jirafas'):
            no_muestras = 15
        elif(animal == 'chimpancés' or animal == 'chimpances'):
            no_muestras = 40
        else:
            no_muestras = 0
        if(no_muestras > 0):
            for valor in range(no_muestras):
                edad_animal = random.uniform(0.1, 56)
                if(edad_animal > 0 and edad_animal <= 1):
                    acum_rango_uno += edad_animal
                    contador_uno += 1
                elif(edad_animal > 1 and edad_animal <= 3):
                    acum_rango_dos += edad_animal
                    contador_dos += 1
                else:
                    acum_rango_tres += edad_animal
                    contador_tres += 1
                edades.append(edad_animal)
                suma_edades += edad_animal
            participacion_uno = round((acum_rango_uno / suma_edades) * 100, 2)
            participacion_dos = round((acum_rango_dos / suma_edades) * 100, 2)
            participacion_tres = round(
                (acum_rango_tres / suma_edades) * 100, 2)
            print('\n---------- RESULTADOS DE LAS MUESTRAS ----------\n')
            print(f'Animal estudiado: {animal.capitalize()}')
            print(f'Tamaño de la muestra: {no_muestras}')
            print(f'% edades entre los 0 - 1 años: {participacion_uno}%')
            print(
                f'% edades de más de 1 año y menos de 3: {participacion_dos}%')
            print(f'% de edades mayor a 3 años: {participacion_tres}%')
            print('Listado de muestras tomadas: ')
            for edad in edades:
                contador += 1
                print(f'Muestra No {contador}: {round(edad,2)}')
        else:
            print('\nNo se suministró un nombre de animal válido (Elefantes,'
                  ' Jirafas, Chimpancés).')
    else:
        print('\nNo se suministró un nombre de animal válido (Elefantes, '
              'Jirafas, Chimpancés).')


print('\n---------- TOMA DE MUESTRAS DE EDADES DE ANIMALES ----------\n')
animal = input('Ingrese nombre de animal a estudiar (Elefantes, '
               'Jirafas, Chimpancés): ')
porcentaje_edades_animales(animal)
