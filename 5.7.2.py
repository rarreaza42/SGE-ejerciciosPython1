#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 5.7.2. Escribir una función que reciba un número entero k e imprima su descomposición en factores primos.
def factoresPrimos(k):
    print "Descomposición factorial de", k
    x = 2
    while (x <= k):
        while (k%x == 0):
            print x
            k = k/x
        x = x+1

factoresPrimos(64)
