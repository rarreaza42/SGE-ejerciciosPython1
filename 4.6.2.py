#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 4.6.2. Escribir una implementación propia de la función abs,
# que devuelva el valor absoluto de cualquier valor que reciba.
def valorAbsoluto(x):
    if x < 0:
        x = x -(x) -(x)
    return x

print valorAbsoluto(-213321)
print valorAbsoluto(34332)