#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 11.10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo
#  (sea de texto o binario) a otro, de modo que quede exactamente igual.
#  Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.
import os, fnmatch

def copiarArchivo(nombreArchivo):
    archivo = open(nombreArchivo, "rb")
    bytes = archivo.read()
    if fnmatch.fnmatch(os.path.basename(archivo.name), "*.txt"):
        archivoNuevo = open("nuevoArchivo.txt", "w")
    elif fnmatch.fnmatch(os.path.basename(archivo.name), "*.bin"):
        archivoNuevo = open("nuevoArchivo.bin", "w")
    for i in bytes:
        i = i.rstrip('\n')
        archivoNuevo.write(i)

copiarArchivo("archivo11.bin")
