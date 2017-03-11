#!/usr/bin/python
#nested functions
#recursive functions executed according to the scope of LEGB
#when the function having same name in different scope
if(0):
	def fun():
		print "outside function"
		def fun():
			print "inside function"
		fun()
	fun()
#function having different names
if(0):
	def fun1():
		print "outside function"
		def fun2():
			print "inside function"
	fun2()
	#fun1.fun2()-> fun1 has no attribute of fun2()
	#fun1(fun2())-> fun2 has not defined because the def of fun2 in another fun1	
#recursive function
if(1):
	def fun():
		print "outside function"
		fun()
