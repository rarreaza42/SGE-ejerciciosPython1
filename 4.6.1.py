#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 4.6.1. Escribir funciones que resuelvan los siguientes problemas:

# 1. Dado un número entero n, indicar si es o no par.
def esPar(n):
    if (n%2 == 0):
        return True
    else:
        return False

# 2. Dado un número entero n, indicar si es o no primo.
def esPrimo(n):
    numDivisores = 0
    for x in range(1, n+1):
        if (n%x == 0):
            numDivisores = numDivisores + 1
    if numDivisores == 2:
        return True
    else:
        return False

print esPar(32)
print esPar(33)
print esPrimo(13)
print esPrimo(16)

