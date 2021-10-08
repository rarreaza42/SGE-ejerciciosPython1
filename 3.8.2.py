#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calcula la cantidad de segundos en un tiempo dado en horas, minutos y segundos.
def aSegundos (horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal


# Calcula la cantidad de horas, minutos y segundos de un tiempo dado en segundos
def aHoras(x):
    hs = x / 3600
    min = (x % 3600) / 60
    seg = (x % 3600) % 60
    return hs, min, seg


print "Hora 1"
h = input("Introduce horas")
m = input("Introduce minutos")
s = input("Introduce segundos")
s1 = aSegundos(h, m, s)

print "Hora 2"
h = input("Introduce horas")
m = input("Introduce minutos")
s = input("Introduce segundos")
s2 = aSegundos(h, m, s)

s3 = s1+s2

(h, m, s) = aHoras(s3)
print "Horas:", h, "Minutos:", m, "Segundos:", s