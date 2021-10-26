#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 9.5.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde
# las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
lista = [("Bien", "Python"), ("Mal", "SQL"), ("Bien", "Java"), ("Regular", "C++"), ("Regular", "CSS")]

def diccionario(lista):
    dic = {}
    cont = 0
    while cont < len(lista):
        t = lista[cont]
        listaVar = [t[1]]
        if t[0] in dic:
            listaVar = dic[t[0]]
            listaVar.append(t[1])
        dic[t[0]] = listaVar
        cont = cont + 1
    return dic

dic = diccionario(lista)
for t in dic:
    print t, ":", dic[t]