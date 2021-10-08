#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 7.6.2. Dominó.

# 1. Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas,
# por ejemplo: (3,4) y (5,4).
def dominoEncaja(tupla1, tupla2):
    num11 = tupla1[0]
    num12 = tupla1[1]
    num21 = tupla2[0]
    num22 = tupla2[1]
    if num11 == num21 or num11 == num22 or num12 == num21 or num12 == num22:
        return True
    else:
        return False

tupla1 = (4, 6)
tupla2 = (7, 9)
tupla3 = (6, 2)
print dominoEncaja(tupla1, tupla2) # false
print dominoEncaja(tupla1, tupla3) # true (comparten el 6)


# 2. Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en una cadena,
# por ejemplo: 3-4 2-5. Nota: utilizar la función split de las cadenas.
def dominoEncaja2(fichas):
    lista = fichas.split(" ")
    ficha1 = lista[0]
    ficha2 = lista[1]
    listaNumeros1 = ficha1.split("-")
    listaNumeros2 = ficha2.split("-")
    num11 = listaNumeros1[0]
    num12 = listaNumeros1[1]
    num21 = listaNumeros2[0]
    num22 = listaNumeros2[1]
    if num11 == num21 or num11 == num22 or num12 == num21 or num12 == num22:
        return True
    else:
        return False

domino1 = "6-7 5-3"
domino2 = "1-9 3-1"
print dominoEncaja2(domino1) # false
print dominoEncaja2(domino2) # true (comparten el 1)
