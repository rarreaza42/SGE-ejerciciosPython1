#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 11.10.1. Escribir un programa, llamado head que reciba un archivo y un número N e imprima
# las primeras N líneas del archivo.
def head(nombreArchivo, n):
    archivo = open(nombreArchivo, "r")
    i = 0
    while i < n:
        linea = archivo.readline().rstrip("\n")
        print linea
        i = i + 1
    archivo.close()

archivo = "archivo1.txt"
head(archivo, 5)

