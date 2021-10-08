#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6.8.2. Escribir funciones que dada una cadena y un caracter:
# Inserte el caracter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r
def separar(cadena, caracter):
    cadena2 = ""
    cont = 1
    for x in cadena:
        if cont < len(cadena):
            cadena2 = cadena2 + x + caracter
        else:
            cadena2 = cadena2 + x
        cont = cont + 1
    print cadena2

# Reemplace todos los espacios por el caracter. Ej: mi archivo de texto.txt y \_ debería devolver mi\_archivo\_de\_texto.txt
def reemplazar(cadena, caracter):
    cadena2 = ""
    for x in cadena:
        if x == " ":
            x = caracter
        cadena2 = cadena2 + x
    print cadena2

# Reemplace todos los dígitos en la cadena por el caracter. Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
def reemplazar2(cadena, caracter):
    cadena2 = ""
    for x in cadena:
        cadena2 = cadena2 + caracter
    print cadena2

# Inserte el caracter cada 3 dígitos en la cadena. Ej. 2552552550 y . debería devolver 255.255.255.0
def cadaTres(cadena, caracter):
    cadena2 = ""
    i = 1
    for x in cadena:
        if i%3 == 0:
            cadena2 = cadena2 + x + caracter
        else:
            cadena2 =  cadena2 + x
        i = i + 1
    print cadena2

cadena = "Me encanta programar en Python"
caracter = "-"
separar(cadena, caracter)
reemplazar(cadena, caracter)
reemplazar2(cadena, caracter)
cadaTres(cadena, caracter)