#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Ejercicio A"
# Calcula la cantidad de segundos en un tiempo dado en horas, minutos y segundos.
def aSegundos (horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal


s = aSegundos(34, 47, 21)
print "Segundos: ", s


print ""
print "Ejercicio B"
# Calcula la cantidad de horas, minutos y segundos de un tiempo dado en segundos
def aHoras(x):
    hs = x / 3600
    min = (x % 3600) / 60
    seg = (x % 3600) % 60
    return hs, min, seg


(h, m, s) = aHoras(4963)
print "Horas:", h, ", Minutos:", m, ", Segundos:", s

