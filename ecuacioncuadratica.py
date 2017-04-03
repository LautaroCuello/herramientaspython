#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os

def ecuacion(a, b, c):
	os.system('cls')
	cuadrado = float(b**2 - 4*a*c)
	if(cuadrado > 0):
		cuadrado = raiz_cuadrada(cuadrado)
		resultado1 = (-b + float(cuadrado))/(2*a)
		resultado2 = (-b - float(cuadrado))/(2*a)
		return "\nEl resultado A(+) es: %0.2f\nY el resultado B(-) es: %0.2f" % (resultado1, resultado2)
	else:
		return "\nLa ecuacion es imposible"

def raiz_cuadrada(x):
	cuadrado = math.sqrt(x)
	return cuadrado

a = raw_input("Ingrese A: ")
b = raw_input("Ingrese B: ")
c = raw_input("Ingrese C: ")
a = float(a)
b = float(b)
c = float(c)

print ecuacion(a, b, c)
