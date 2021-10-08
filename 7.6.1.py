#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 7.6.1. Escribir una función que reciba una tupla de elementos e indique si se encuentran
# ordenados de menor a mayor o no.
def estaOrdenada(tupla):
    longitud = len(tupla)
    estaOrdenada = True
    pos = 0
    elemento = tupla[pos]
    while pos < longitud-1 and estaOrdenada == True:
        pos = pos + 1
        if(elemento > tupla[pos]):
            estaOrdenada = False
        elemento = tupla[pos]
    return estaOrdenada

tupla = (11, 3, 12, 68, 23)
print estaOrdenada(tupla) # false
tupla2 = (5, 34, 67, 32145)
print estaOrdenada(tupla2) # true
