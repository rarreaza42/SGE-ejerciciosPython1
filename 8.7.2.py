#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 8.7.2. Escribir una función que reciba una lista de números no ordenada, que:

lista = [1, 3, 4, 5, 3, 7, 8, 3, 7, 4, 3, 7, 7]

# 1. Devuelva el valor máximo.
def valorMax(lista):
    max = lista[0]
    for z in lista:
        if z > max:
            max = z
    return max

print "Valor máximo: " + str(valorMax(lista))

# 2. Devuelva una tupla que incluya el valor máximo y su posición.
def valorMaxPos(lista):
    pos = 0
    cont = 0
    max = lista[0]
    for z in lista:
        if z > max:
            max = z
            pos = cont
        cont = cont + 1
    t = (max, pos)
    return t

print "Tupla valor máximo y posición: " + str(valorMaxPos(lista))

# 3. ¿Qué sucede si los elementos son cadenas de caracteres? Nota: no utilizar lista.sort()
listaCaracteres = ["dasf", "ser", "trewertew", "fbtydbf", "srfser", "d", "serwe"]
def valorMaxPos2(lista):
    pos = 0
    cont = 0
    max = lista[0]
    for z in lista:
        if z > max:
            max = z
            pos = cont
        cont = cont + 1
    t = (max, pos)
    return t

print "Tupla valor máximo y posición: " + str(valorMaxPos2(listaCaracteres))

# Devuelve la cadena de caracteres más de mayor longitud