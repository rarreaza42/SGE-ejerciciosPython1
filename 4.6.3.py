#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Este import sirve para imprimir por consola sin saltos de línea
import sys

# Ejercicio 4.6.3. Escribir una función que reciba por parámetro una dimensión n,
# e imprima la matriz identidad correspondiente a esa dimensión.
def matrizIdentidad(n):
    cont = 0
    for x in range(0, n):
        for x in range(0, n):
            if cont == x:
                sys.stdout.write(str(1))
            else:
                sys.stdout.write(str(0))
        print ""
        cont = cont +1

matrizIdentidad(5)