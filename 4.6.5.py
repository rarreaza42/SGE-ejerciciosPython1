#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 4.6.5. Escribir funciones que resuelvan los siguientes problemas:

# Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4,
# pero no si es divisible por 100, excepto que también sea divisible por 400.
def esBisiesto(x):
    if (x%4 == 0 and x%100 != 0) or (x%4 == 0 and x%400 == 0):
        return True
    else:
        return False

print "1"
print esBisiesto(2019)

# Dado un mes, devolver la cantidad de dias correspondientes.
def diasMes(mes, agno):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or
        mes == 10 or mes == 12):
        return 31
    else:
        if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
            return 30
        else:
            if esBisiesto(agno):
                return 29
            if not esBisiesto(agno):
                return 28
            else:
                return -1

print "2"
print diasMes(8, 2021)
print diasMes(2, 2021)
print diasMes(2, 2020)
print diasMes(4, 2021)

# Dada una fecha (dia, mes, año), indicar si es válida o no.
def fechaCorrecta(dia, mes, agno):
    if diasMes(mes, agno) == -1:
        return False
    elif dia <= diasMes(mes, agno) and dia > 0:
        return True
    else:
        return False

print "3"
print fechaCorrecta(29, 2, 2021) #falsa (no bisiesto
print fechaCorrecta(29, 2, 2020) #verdadera (bisiesto)
print fechaCorrecta(132312, 8, 2021) #falsa (días alto)
print fechaCorrecta(29, 321321, 2021) # falsa (mes incorrecto)
print fechaCorrecta(-23, 2, 2021) # falsa (días bajo)

# Dada una fecha, indicar los dias que faltan hasta fin de mes.
def finMes(dia, mes, agno):
    if fechaCorrecta(dia, mes, agno):
        dias = diasMes(mes, agno)
        diasFaltan = dias - dia
        return diasFaltan
    else:
        return -1

print "4"
print finMes(29, 2, 2021) # Devuelve -1 porque es fecha inválida
print finMes(15, 2, 2021) # Devuelve 13

# Dada una fecha, indicar los dias que faltan hasta fin de año.
def finAgno(dia, mes, agno):
    if fechaCorrecta(dia, mes, agno):
        if esBisiesto(agno):
            diasAgno = 366
        else:
            diasAgno = 365
        acumuladorDias = dia
        for x in range(1, mes):
            acumuladorDias = acumuladorDias + diasMes(x, agno)
        return diasAgno - acumuladorDias
    else:
        return -1

print "5"
print finAgno(3213, 12, 2020) # Día inválido
print finAgno(27, 12, 2021) # Válido: 4 días
print finAgno(4, 2, 2020) # Válido: 331 días

# Dada una fecha, indicar la cantidad de dias transcurridos en ese año hasta esa fecha.
def diasTranscurridos(dia, mes, agno):
    if fechaCorrecta(dia, mes, agno):
        acumuladorDias = dia
        for x in range(1, mes):
            acumuladorDias = acumuladorDias + diasMes(x, agno)
        return acumuladorDias
    else:
        return -1

print "6"
print diasTranscurridos(3213, 12, 2020) # Día inválido
print diasTranscurridos(31, 12, 2020) # Válido: año bisiesto, 366 días
print diasTranscurridos(4, 2, 2020) # Válido:35 días

# Dadas dos fechas (dia1, mes1, año1, dia2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y dias.
def diasEntreFechas(dia1, mes1, agno1, dia2, mes2, agno2):
    # if((agno1 > agno2) or (agno1 == agno2 and mes1 > mes2) or (agno1 == agno2 and mes1 == mes2 and dia1 > dia2)):
    if(agno1 > agno2):
        acumuladorDias = finAgno(dia2, mes2, agno2) + diasTranscurridos(dia1, mes1, agno1) + (agno1 - agno2 -1)
        for x in range(agno2+1, agno1):
            if esBisiesto(x):
                acumuladorDias = acumuladorDias + 366
            else:
                acumuladorDias = acumuladorDias + 365
    elif (agno2 > agno1):
        acumuladorDias = finAgno(dia1, mes1, agno1) + diasTranscurridos(dia2, mes2, agno2) + (agno2 - agno1 -1)
        for x in range(agno1+1, agno2):
            if esBisiesto(x):
                acumuladorDias = acumuladorDias + 366
            else:
                acumuladorDias = acumuladorDias + 365
    elif (agno1 == agno2 and mes1 > mes2):
        acumuladorDias = finMes(dia2, mes2, agno2) + (diasMes(mes1, agno1) - finMes(dia1, mes1, agno1))
        for x in range(mes2+1, mes1):
            acumuladorDias = acumuladorDias + diasMes(x, agno1)
    elif (agno1 == agno2 and mes2 > mes1):
        acumuladorDias = finMes(dia1, mes1, agno1) + (diasMes(mes2, agno2) - finMes(dia2, mes2, agno2))
        for x in range(mes1+1, mes2):
            acumuladorDias = acumuladorDias + diasMes(x, agno2)
    elif (agno1 == agno2 and mes2 == mes1 and dia1 > dia2):
        acumuladorDias = dia1 - dia2
    elif (agno1 == agno2 and mes2 == mes1 and dia2 > dia1):
        acumuladorDias = dia2 - dia1
    return acumuladorDias

print "7"
print "Días:", diasEntreFechas(2, 7, 1997, 28, 9, 2018)



