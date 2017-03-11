#!/usr/bin/python
class A:
	def __init__(self):
		print "In __init__ function"
		self.x = 10
		self._y = 20
		self.__z = 30
		#print self.__z
		#print self._y
		#print self.x
	def fun1(self):
		print "In fun1 function"
	def _fun2(self):
		print "In _fun2 function"
	def __fun3(self):
		print "in __fun3 function"
		#self.__fun3()
m = A()#A.__init__(m)
print m.x
print m._y
print m._A__z
m.fun1()#fun1(m)
m._fun2()
m._A__fun3()




''' output of this -----
		print m.__z -> attribute error
		commenting that----
			error when invoking the fun3 
			m.__fun3 -> attribute error
				

	Reason- __ represents the access specifier-> fully private
				we cant access any attribute and any method 
				associate to its object outside of the callings

		"Inside of method we can access" 		'''
