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

# 3. Una empresa se requiere calcular el salario semanal de cada uno de los n
# obreros que laboran en ella. El salario se obtiene de la siguiente forma:
# a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
# b. Si trabaja mas de 40 horas se le paga $20 por cada una de
# las primeras 40 horas y $25 por cada hora extra

# Supuestos: Para el número random se ha tenido en cuenta una edad entre 1 y 60
# debido a:
# Horas ordinarias legales permitidas en Colombia: 48 por semana
# Horas extras legales permitidas en Colombia: 12 por semana
# Es decir, total horas legales permitidad en Colombia a la semana: 60 horas.


def calcular_salario(no_trabajadores):
    horario_ordinario = 40
    valor_hora_ordinaria = 20
    valor_hora_extra = 25
    total_salario = 0
    total_salario_ordinario = 0
    total_salario_extra = 0
    total_salario_trabajadores = 0
    if(no_trabajadores > 0):
        for trabajador in range(no_trabajadores):
            horas_laboradas = random.randint(1, 60)
            if(horas_laboradas <= horario_ordinario):
                horas_ordinarias = horas_laboradas
                horas_extras = 0
                salario_ordinario = valor_hora_ordinaria * horas_ordinarias
                salario_extra = valor_hora_extra * horas_extras
                total_salario = salario_ordinario + salario_extra
            else:
                horas_ordinarias = 40
                horas_extras = horas_laboradas - horario_ordinario
                salario_ordinario = valor_hora_ordinaria * horas_ordinarias
                salario_extra = valor_hora_extra * horas_extras
                total_salario = salario_ordinario + salario_extra
            print(f'\n--- Datos del trabajador No. {trabajador+1} ---\n')
            print(f'Horas laboradas: {horas_laboradas}')
            print(f'Horas ordinarias laboradas: {horas_ordinarias}')
            print(f'Horas extras laboradas: {horas_extras}')
            print(f'Salario ord. laborado: {salario_ordinario}')
            print(f'Salario extra laborado: {salario_extra}')
            print(f'Salario total: {total_salario}\n')
            total_salario_ordinario += salario_ordinario
            total_salario_extra += salario_extra
            total_salario_trabajadores += total_salario
        print('\n--- Resumen de liquidación de nómina del personal ---\n')
        print(f'Salario total ordinario: {total_salario_ordinario}')
        print(f'Salario total extra: {total_salario_extra}')
        print(f'Salario total general: {total_salario_trabajadores}')
    else:
        print('\nPara realizar un cálculo válido de nómina se debe ingresar'
              ' un número de trabajadores igual o mayor a 1.')


print('\n---------- TOMA DE MUESTRAS DE EDADES DE ANIMALES ----------\n')
no_trabajadores = int(input('Ingrese número de trabajadores (mayor a 0): '))
calcular_salario(no_trabajadores)

# 4. Calcular el promedio de edades de hombres, mujeres y de todo un grupo
# de alumnos.


def calcular_promedio_edades(no_personas=0):
    if(no_personas > 0):
        no_hombres = 0
        no_mujeres = 0
        suma_hombres = 0
        suma_mujeres = 0
        suma_total = 0
        promedio_edad_hombres = 0
        promedio_edad_mujeres = 0
        promedio_edad_total = 0
        edades_hombres = []
        edades_mujeres = []
        for personal in range(no_personas):
            genero = random.randint(0, 1)
            edad = random.randint(1, 118)
            if(genero > 0):
                suma_hombres += edad
                no_hombres += 1
                edades_hombres.append(edad)
            else:
                suma_mujeres += edad
                no_mujeres += 1
                edades_mujeres.append(edad)
            suma_total += edad
        if(no_hombres > 0):
            promedio_edad_hombres = suma_hombres/no_hombres
        else:
            promedio_edad_hombres = 0
        if(no_mujeres > 0):
            promedio_edad_mujeres = suma_mujeres/no_mujeres
        else:
            promedio_edad_mujeres = 0
        promedio_edad_total = suma_total/no_personas
        print('\n--- Resumen de estadísticas de promedio de edades del grupo'
              '---\n')
        print(f'Total población: {no_personas}')
        print(f'Número de hombres: {no_hombres}')
        print(f'Número de mujeres: {no_mujeres}')
        print(f'Promedio de edad de hombres del grupo: '
              f'{promedio_edad_hombres:.2f}')
        print(f'Promedio de edad de mujeres del grupo: '
              f'{promedio_edad_mujeres:.2f}')
        print(f'Promedio de edad del grupo: {promedio_edad_total:.2f}')
        print('\n------ Detalle de listado de edades de la población ------\n')
        print(f'Número de hombres: {edades_hombres}')
        print(f'Número de mujeres: {edades_mujeres}')
    else:
        print('\nPara realizar un cálculo válido del promedio de edad de un '
              'grupo, el número de la población debe ser igual o mayor a 1.')


print('\n------ TOMA DE MUESTRAS DE EDADES DE UN GRUPO DE PERSONAS ------\n')
no_personas = int(input('Ingrese número de personas (mayor a 0): '))
calcular_promedio_edades(no_personas)
