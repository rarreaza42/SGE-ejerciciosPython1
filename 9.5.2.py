#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 9.5.2. Diccionarios usados para contar.
#
# Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra
# en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver:
# 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
import random


def numAparicionesPalabra(cadena):
    listaPalabras = cadena.split()
    dic = {}
    pos = 0
    for x in listaPalabras:
        cont = 1
        if x in dic:
            cont = dic[x] + 1
        dic[x] = cont
    return dic

print "1)"
cadena = "hola que tal que voy a ir a tu casa a ver que tal va que voy ya"
dic = numAparicionesPalabra(cadena)
for t in dic:
    print t, ":", dic[t]

# Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto,
# y los devuelva en un diccionario.
def numAparicionesCaracter(cadena):
    dic = {}
    pos = 0
    for x in cadena:
        cont = 1
        if x in dic:
            cont = dic[x] + 1
        dic[x] = cont
    return dic

print ""
print "2)"
cadena2 = "esternocleidomastoideo"
dic = numAparicionesCaracter(cadena2)
for t in dic:
    print t, ":", dic[t]

# Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva
# la cantidad de veces que se observa cada valor de la suma de los dos dados. Nota: utilizar el módulo random
# para obtener tiradas aleatorias.
import random

def sumaDados(numTiradas):
    dic = {}
    cont = 0
    while cont < numTiradas:
        suma = random.randint(1, 6) + random.randint(1, 6)
        if suma in dic:
            dic[suma] = dic[suma] + 1
        else:
            dic[suma] = 1
        cont = cont + 1
    return dic

print ""
print "3)"
dic = sumaDados(20)
for x in dic:
    print x, ":", dic[x]