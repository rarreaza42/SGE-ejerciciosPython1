#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 7.6.3. Campaña electoral
#
# Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje
# Estimado , vote por mí.
tuplaNombres = ("Rubén", "Souhail", "Ossama", "Alexander", "Alberto", "Jesús", "Radu", "Rufino", "Joaquín")
def votePorMi(tuplaNombres):
    for i in tuplaNombres:
        print "Estimado " + i + ", vote por mí"

print "1"
votePorMi(tuplaNombres)

# Escribir una función que reciba una tupla con nombres, una posición de origen p y una cantidad n,
# e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p.



# Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, para ello,
# deberán recibir una tupla de tuplas, conteniendo el nombre y el género.