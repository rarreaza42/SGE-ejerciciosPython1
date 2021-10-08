#!/usr/bin/env python
# -*- coding: utf-8 -*-

def aHsMinSeg(x):
    """ Dada una duración en segundos sin fracciones
        (la función debe invocarse con números enteros)
        se la convierte a horas, minutos y segundos """
    hs = x / 3600
    min = (x % 3600) / 60
    seg = (x % 3600) % 60
    return hs, min, seg  # hola


(h, m, s) = aHsMinSeg(3661)
print "Horas:", h, ", Minutos:", m, ", Segundos:", s
