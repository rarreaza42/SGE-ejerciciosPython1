#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos. Por ejemplo,
# si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre ellos.
def mayorProducto(a, b, c, d):
    mayorP = a*b
    for x in [a, b, c, d]:
        for y in [a, b, c, d]:
            e = x*y
            if(e > mayorP):
                mayorP = e
    return mayorP


a = input("Introduce el primer número")
b = input("Introduce el segundo número")
c = input("Introduce el tercer número")
d = input("Introduce el cuarto número")
e = mayorProducto(a, b, c, d)
print ("El mayor producto es", e)