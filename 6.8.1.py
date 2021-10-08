#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6.8.1. Escribir funciones que dada una cadena de caracteres:
# Imprima los dos primeros caracteres.
def dosPrimeros(cadena):
    print cadena[:2]

# Imprima los tres últimos caracteres.
def tresUltimos(cadena):
    print cadena[-3:]

# Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
def cadaDos(cadena):
    cadena2 = ""
    i = 0
    for x in cadena:
        if i%2 == 0:
            cadena2 = cadena2 + x
        i = i + 1
    print cadena2

# Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh
def inverso(cadena):
    cadena2 = ""
    for x in cadena:
        cadena2 = x + cadena2
    print cadena2

# Imprima la cadena en un sentido y en sentido inverso. Ej: reflejo imprime reflejoojelfer.
def inverso2(cadena):
    cadena2 = ""
    for x in cadena:
        cadena2 = x + cadena2
    print cadena + cadena2


cadena = "Me encanta programar en Python"
dosPrimeros(cadena)
tresUltimos(cadena)
cadaDos(cadena)
inverso(cadena)
inverso2(cadena)