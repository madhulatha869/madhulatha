#!/usr/bin/python
#exp1
if(0):
	def test1():
		#print "experiment 1 executing test1 function"
		return "I am in test1 function"
	test1()
	print test1()
#exp2
if(1):
	def test2():
		"this is test function"		
#exp3
if(0):
#	def test3(a=10,b)://function creating error
	def test3(a,b=20):
		print a,b
#	test3(b=10,a=20)
#	test3()     invoking error - function atleast have one argument
	test3(a=40)
#exp4
if(0):
	x = 100
	print x
	def test4():
		global x
		x = 200
		print x
	test4()
	print x
