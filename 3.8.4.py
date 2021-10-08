#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1) Escribir una función que dado un vector al origen (definido por sus puntos x, y),
# devuelva la norma del vector, dada por (x^2 + y^2) ^ 1/2
def normaVector(x, y):
    return (x^2 + y^2) ^ 1/2

# 2) Escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2),
# devuelva la resta de ambos (debe devolver un par de valores).
def restaVectores(x1, y1, x2, y2):
    if x1 > x2:
        x3 = x1 - x2
    else:
        x3 = x2 - x1
    if y1 > y2:
        y3 = y1 - y2
    else:
        y3 = y2 - y1
    return x3, y3

# 3) Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2),
# devuelva la distancia entre ambos.
def distancia(x1, y1, x2, y2):
    x3, y3 = restaVectores(x1, y1, x2, y2)
    return normaVector(x3, y3)

# 4) Escribir una función que reciba un vector al origen (definido por sus puntos x, y)
# y devuelva un vector equivalente, normalizado (debe devolver un par de valores).
def vectorEquivalente(x1, y1, x2, y2):
    for x in (x1, y1, x2, y2):
        x = x+1
    punto1 = normaVector(x1, y1)
    punto2 = normaVector(x2, y2)
    return punto1, punto2

# 5) Utilizando las funciones anteriores (b y d), escribir una función que dados dos puntos en el plano
# (x1, y1 y x2, y2), devuelva el vector dirección unitario correspondiente a la recta que los une.
def VectorUnitario(x1, y1, x2, y2):
    x3, y3 = distancia(x1, y1, x2, y2)
    norma = normaVector(x3, y3)
    return (x3 / norma), (y3/norma)

# 6) Escribir una función que reciba un punto (x, y), una dirección unitaria de una recta (dx, dy)
# y un punto perteneciente a esa recta (cx, cy) y devuelva la proyección del punto sobre la recta.


