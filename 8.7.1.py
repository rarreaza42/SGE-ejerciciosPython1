#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 8.7.1. Escribir una función que reciba una lista desordenada y un elemento, que:

lista = [1, 3, 4, 5, 3, 7, 8, 3, 7, 4, 3, 7, 7]
x = 7

# 1. Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de
# coincidencias encontradas.
def numCoincidencias(lista, x):
    coincidencias = 0
    for z in lista:
        if z == x:
            coincidencias = coincidencias + 1
    return coincidencias

print "Coincidencias: " + str(numCoincidencias(lista, x))

# 2. Busque la primera coincidencia del elemento en la lista y devuelva su posición.
def primeraCoincidencia(lista, x):
    pos = 0
    for z in lista:
        if z == x:
            return pos
        pos = pos + 1

print "Primera coincidencia: " + str(primeraCoincidencia(lista, x))

# 3. Utilizando la función anterior, busque todos los elementos coincidan con el pasado por
# parámetro y devuelva una lista con las posiciones.
def listaPosiciones(lista, x):
    listaB = []
    pos = 0
    posB = 0
    for z in lista:
        if z == x:
            listaB.insert(posB, pos)
            posB = posB + 1
        pos = pos + 1
    return listaB

print "Lista posiciones: " + str(listaPosiciones(lista, x))