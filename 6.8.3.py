#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6.8.3. Modificar las funciones anteriores, para que reciban un parámetro que indique
# la cantidad máxima de reemplazos o inserciones a realizar. (Modificaremos el cuarto)
def cambio(cadena, caracter, maxCambios):
    cadena2 = ""
    i = 1
    cont = 0
    for x in cadena:
        if cont < maxCambios:
            if i%3 == 0:
                cadena2 = cadena2 + x + caracter
                cont = cont + 1
            else:
                cadena2 = cadena2 + x
        else:
            cadena2 = cadena2 + x
        i = i + 1
    print cadena2

cadena = "Me encanta programar en Python"
caracter = "-"

cambio(cadena, caracter, 5)