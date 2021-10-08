#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 5.7.3. Manejo de contraseñas

# Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña,
# y no le permita continuar hasta que la haya ingresado correctamente.
import time


def contrasegna():
    contra = "pythonrules"
    cont = raw_input("Introduce la contraseña.")
    while (cont != contra):
        print "Contraseña incorrecta."
        cont = raw_input("Introduce la contraseña.")
    print "Contraseña correcta. Adelante."

# contrasegna()

# Modificar el programa anterior para que solamente permita una cantidad fija de inten-tos.
def contrasegna2():
    contra = "pythonrules"
    intentos = 0
    cont = raw_input("Introduce la contraseña.")
    while (cont != contra and intentos < 3):
        intentos = intentos +1
        print "Contraseña incorrecta."
        cont = raw_input("Introduce la contraseña (intento " + repr(intentos) + ").")
    if(cont == contra):
        print "Contraseña correcta. Adelante."
    else:
        print "No te quedan más intentos."

# contrasegna2()

# Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor,
# utilizando la función sleep del módulo time.
def contrasegna3():
    contra = "pythonrules"
    intentos = 0
    dormir = 0
    cont = raw_input("Introduce la contraseña.")
    while (cont != contra and intentos < 3):
        intentos = intentos +1
        dormir = dormir + 1
        time.sleep(dormir)
        print "Contraseña incorrecta."
        cont = raw_input("Introduce la contraseña (intento " + repr(intentos) + ").")
    if(cont == contra):
        print "Contraseña correcta. Adelante."
    else:
        time.sleep(dormir+1)
        print "No te quedan más intentos."

# contrasegna3()

# Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no
# la contraseña correctamente, mediante un valor booleano (True o False).
def contrasegna4():
    contra = "pythonrules"
    intentos = 0
    dormir = 0
    cont = raw_input("Introduce la contraseña.")
    while (cont != contra and intentos < 3):
        intentos = intentos +1
        dormir = dormir + 1
        time.sleep(dormir)
        print "Contraseña incorrecta."
        cont = raw_input("Introduce la contraseña (intento " + repr(intentos) + ").")
    if(cont == contra):
        return True
    else:
        time.sleep(dormir+1)
        return False

if contrasegna4() == True:
    print "Correcto. Adelante"
else:
    print "Incorrecto. Se han acabado los intentos"