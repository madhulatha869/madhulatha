#!/usr/bin/python
# a is first number and b is second number
def add(a,b):
	try:
		a+b
		raise TypeError
	except TypeError:
		print "TypeError"
	else:
		return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	try:
		a/b
		raise ZeroDivisionError
	except ZeroDivisionError:
		print "ZeroDivisionError"
	else:
		return a/b
def sin(num):
	import math
	return math.sin(math.radians(num))
def cos(num):
	import math
	return math.cos(math.radians(num))
def sqrt(num):
	import math
	return math.sqrt(num)
def power_of(a,b):
	import math
	return math.pow(a,b)
def go_back():
	import calculator_display
	calculator_display.main
