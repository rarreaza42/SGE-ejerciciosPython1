#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6.8.4. Escribir una función que reciba una cadena que contiene un largo número entero
# y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe 1234567890,
# debe devolver 1.234.567.890.
def aMillares(numero):
    numeroAlReves = numero[::-1]
    numeroAlReves2 = ""
    i = 1
    for x in numeroAlReves:
        if (i-1)%3 == 0 and i-1 != 0:
            numeroAlReves2 = numeroAlReves2 + "." + x
        else:
            numeroAlReves2 = numeroAlReves2 + x
        i = i + 1
    numeroFinal = numeroAlReves2[::-1]
    return numeroFinal

print aMillares("1242345236453465367")