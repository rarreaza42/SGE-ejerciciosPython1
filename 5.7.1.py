#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 5.7.1. Escribir un programa que reciba una a una las notas del usuario,
# preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.
def mediaNotas():
    masNotas = "si"
    acumulador = 0
    contador = 0
    while (masNotas == "si"):
        nota = input("Introduce tu nota")
        contador = contador +1
        acumulador = acumulador + nota
        masNotas = raw_input("¿Quieres seguir? <si-no>: ")
    media = acumulador / contador
    print "La media es", media

mediaNotas()


