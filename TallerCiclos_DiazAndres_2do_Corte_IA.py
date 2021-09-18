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

# 5. Encontrar el menor valor de un conjunto de n números dados.


def calcular_menor_valor(no_valores=0):
    if(no_valores > 0):
        valores = []
        for item in range(no_valores):
            valor_ingresar = random.randint(0, 100)
            valores.append(valor_ingresar)
        menor_valor = valores[0]
        for valor in range(no_valores - 1):
            if(valores[valor] < menor_valor):
                menor_valor = valores[valor]
        print('\n------ Resultados de los comparativos ------\n')
        print(f'La cantidad de valores es: {no_valores}')
        print(f'Los valores son: {valores}')
        print(f'El menor de los valores es: {menor_valor}')
    else:
        print('\nPara realizar una validación correcta la cantidad de números '
              'a evaluar debe ser igual o mayor a 1.')


print('\n------ COMPARATIVO DE VALORES (EVALUAR EL MENOR) ------\n')
no_valores = int(input('Ingrese la cantidad de números a evaluar: '))
calcular_menor_valor(no_valores)

# 6. Cinco miembros de un club contra la obesidad desean saber cuanto han
# bajado o subido de peso desde la última vez que se reunieron. Para esto se
# debe realizar un ritual de pesaje en donde cada uno se pesa en diez
# básculas distintas para así tener el pormedio mas exacto de su peso. Si
# existe diferencia positiva entre este promedio de peso y el peso de la última
# vez que se reunieron, significa que subieron de peso. Pero si la diferencia
# es negativa, significa que bajaron. Lo que el problema requere es que por
# cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
# cantidad de kilos que subió o bajó de peso.

# Supuestos: Se trabaja bajo el supuesto de que el peso de la persona puede
# variar en una tolerancia de +-4 kilos. Así mismo para simular la tolerancia
# de las básculas, se tendrá en cuenta un rango de entre +-3%.
# Las pesonas pertenecen a un grupo de 1.65 mts de altura promedio, con lo cual
# un peso entre 80 y 100 se considera padecer obesidad tipo 1 a 2, es decir, se
# simulara el rango de peso peso_inicial de la persona en dicho rango de peso.


def calcular_peso(no_personas=0):
    if(no_personas > 0):
        no_basculas = 10
        for persona in range(no_personas):
            peso_bascula = 0
            pesos = []
            suma_pesos = 0
            promedio_peso = 0
            tolerancia_peso = round(random.uniform(-4, 4), 2)
            peso_inicial = round(random.uniform(80, 100), 2)
            respuesta = ""
            variacion_peso = 0
            diferencia_peso = 0
            for peso in range(no_basculas):
                tolerancia_bascula = random.uniform(-0.03, 0.03)
                variacion_peso = tolerancia_peso * tolerancia_bascula
                peso_bascula = (tolerancia_peso+variacion_peso) + peso_inicial
                pesos.append(round(peso_bascula, 2))
                suma_pesos += peso_bascula
            promedio_peso = round(suma_pesos/no_basculas, 2)
            diferencia_peso = abs(peso_inicial - promedio_peso)
            if((peso_inicial-promedio_peso) > 0):
                respuesta = "La persona bajó de peso"
            elif((peso_inicial-promedio_peso) < 0):
                respuesta = "La persona subió de peso"
            else:
                respuesta = "La persona mantuvo el mismo peso"
            print(f'\n--- Resumen del seguimiento al peso de persona No '
                  f'{persona + 1} ---\n')
            print(f'Peso incial: {peso_inicial} kilos')
            print(f'Toma de pesos (Kg) en las {no_basculas} básculas:'
                  f' {pesos}')
            print(f'Peso promedio actual: {promedio_peso} kilos')
            print(f'{respuesta} ({round(diferencia_peso,2)} kilos)')
    else:
        print('\nPara realizar el cálculo correcto del peso de las personas la'
              ', cantidad de personas en el grupo debe ser igual o mayor a 1.')


print('\n--------- CLUB CONTRA LA OBESIDAD (SEGUIMIENTO)  ---------')
no_personas = int(input('Ingrese número de personas en el grupo: '))
calcular_peso(no_personas)

# 7. En un supermercado una ama de casa pone en su carrito los artículos que
# va tomando de los estantes. La señora quiere asegurarse de que el cajero
# le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
# artículo anota su precio junto con la cantidad de artículos iguales que ha
# tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
# que irá gastando en los demás artículos, hasta que decide que ya tomó
# todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
# compra.


def precios_articulos(articulo, precio, cantidad, total_precio):
    if(len(articulo) > 0 and len(precio) > 0 and len(cantidad) > 0
       and len(total_precio) > 0):
        respuesta = ""
        cuenta = 0
        precio_total = 0
        for valor in range(len(articulo)):
            precio_total += total_precio[valor]
            cuenta += 1
            respuesta = respuesta + 'Artículo No ' + str(cuenta) + ': ' + \
                articulo[valor] + ', Precio Unitario: $' + \
                str(precio[valor]) + ', Cantidad comprada: ' + \
                str(cantidad[valor]) + ', Precio total compra: $' + \
                str(total_precio[valor]) + '\n'
        print('\n------- Resumen de la compra de la ama de casa -------\n')
        print(respuesta)
        print(f'El precio total de la compra es: ${round(precio_total,2)}')
    else:
        print('Información suministrada inválida.')


def comprar():
    respuesta = 1
    articulos = []
    precios = []
    cantidades = []
    total_precio = []
    while (respuesta != 2):
        articulo = input('Ingrese nombre del artículo: ')
        precio = float(input('Ingrese precio del artículo: '))
        cantidad = int(input('Ingrese cantidad: '))
        articulos.append(articulo)
        precios.append(precio)
        cantidades.append(cantidad)
        total_precio.append(precio*cantidad)
        respuesta = int(
            input('1. Comprar más artículos\n2. Finalizar compra \n> '))
    precios_articulos(articulos, precios, cantidades, total_precio)


# 8. Un teatro otorga descuentos según la edad del cliente, determinar la
# cantidad del dinero que el teatro deja de percibir por cada una de las
# categorias. Tomar en cuenta que los niños menores de 5 años no pueden
# entrar al teatro y que existe un precio único en los asientos.
# Los descuentos se hacen tomando en cuenta el siguiente cuadro:
"""
-------------------------------------
|      Edad         |  % Descuento  |
------------------------------------
|      5 - 14       |      35%      |
|     15 - 19       |      25%      |
|     20 - 45       |      10%      |
|     46 - 65       |      25%      |
|  66 en adelante   |      35%      |
-------------------------------------
"""

# Generar edades aleatorias


def generar_edad():
    edad = random.randint(5, 118)
    return edad


# Calcular descuentos


def calcular_descuentos(no_clientes=0, precio_entradas=0):
    if(no_clientes > 0 and precio_entradas > 0):
        descuento_uno = 0
        descuento_dos = 0
        descuento_tres = 0
        descuento_cuatro = 0
        descuento_cinco = 0
        descuento_total = 0
        resultado = {'entre 5-14 años': 0,
                     'entre 15-19 años': 0,
                     'entre 20-45 años': 0,
                     'entre 46-65 años': 0,
                     'de 66 años en adelante': 0,
                     'listado de edades': []}
        for valor in range(no_clientes):
            edad = generar_edad()
            if(edad >= 5 and edad <= 14):
                descuento_uno = precio_entradas * 0.35
                resultado['entre 5-14 años'] += descuento_uno
            elif(edad >= 15 and edad <= 19):
                descuento_dos = precio_entradas * 0.25
                resultado['entre 15-19 años'] += descuento_dos
            elif(edad >= 20 and edad <= 45):
                descuento_tres = precio_entradas * 0.10
                resultado['entre 20-45 años'] += descuento_tres
            elif(edad >= 46 and edad <= 65):
                descuento_cuatro = precio_entradas * 0.25
                resultado['entre 46-65 años'] += descuento_cuatro
            else:
                descuento_cinco = precio_entradas * 0.35
                resultado['de 66 años en adelante'] += descuento_cinco
            resultado['listado de edades'].append(edad)
        print('\n------ Resumen financiero de descuento de entradas ------\n')
        print(f'Cantidad de personas que ingresaron al teatro: {no_clientes}')
        print(f'Precio estándar de la entrada: ${precio_entradas}')
        for llave, valor in resultado.items():
            if('años' in llave):
                print(f'Total Descuentos por rango de edad {llave}:'
                      f' ${round(valor,2)}')
                descuento_total += valor
        res = {key: resultado[key] for key in resultado.keys()
               & {'listado de edades'}}
        print(f'valor total de los decuentos: ${round(descuento_total,2)}')
        print(f"Lista de edades de clientes: {res.get('listado de edades')}")
    else:
        print('\nEl número de personas que entran al teatro y el precio de'
              ' las entradas debe ser mayor a cero.')


print('\n--------- ESTADO DE RESULTADO FINANCIERO DE DESCUENTOS  ---------\n')
no_clientes = int(input('Ingrese número de clientes del teatro: '))
precio_entradas = float(input('Ingrese precio de las entradas: '))
calcular_descuentos(no_clientes, precio_entradas)

# 9. Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
# siguiente tabla:

"""
-------------------------------------
|   Valor vendido   |   Comisión    |
------------------------------------
| x <= 20 Millones  |      10%      |
|   20 < x < 40     |      15%      |
|   40 <= x < 80    |      20%      |
|   80 <= x < 160   |      25%      |
|      > 160        |      30%      |
-------------------------------------
"""

# Realice un método que diga cuanto vendió y la comisión de los 100
# vendedores que tiene la empresa.


def calcular_comision(valor_vendido):
    valor_comision = 0
    if(valor_vendido <= 20000000):
        valor_comision = valor_vendido * 0.1
    elif(valor_vendido > 20000000 and valor_vendido < 40000000):
        valor_comision = valor_vendido * 0.15
    elif(valor_vendido >= 40000000 and valor_vendido < 80000000):
        valor_comision = valor_vendido * 0.2
    elif(valor_vendido >= 80000000 and valor_vendido < 160000000):
        valor_comision = valor_vendido * 0.25
    else:
        valor_comision = valor_vendido * 0.3
    return valor_comision


def ventas():
    cantidad_empleados = 100
    valor_vendido = 0
    total_vendido = 0
    total_comisiones = 0
    respuesta = ""
    for i in range(cantidad_empleados):
        valor_vendido = random.uniform(1000000, 320000000)
        comision = calcular_comision(valor_vendido)
        respuesta += 'Empleado No. ' + str(i+1) + '\n'\
            'Valor vendido: ' + '$' + str(round(valor_vendido, 2)) + '\n'\
            'Valor Comisión: ' + '$' + str(round(comision, 2)) + '\n'
        total_vendido += valor_vendido
        total_comisiones += comision
    print('\n-------- Resumen de estado de comisiones --------\n')
    print(f'{respuesta}\n ---------- Valores totalizados ----------')
    print(f'Total vendido por todos los empleados es: ${total_vendido:,.2f}')
    print(f'Total de las comisiones de todos los empleados es:'
          f' ${total_comisiones:,.2f}')
