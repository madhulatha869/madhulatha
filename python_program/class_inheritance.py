#!/usr/bin/python
class shape():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def area(self):
		return self.x * self.y
	def perimeter(self):
		return 2*self.x + 2*self.y
#myshape = shape(5,6)
#print myshape.area()
#print myshape.perimeter()'''
class square(shape):
	def __init__(self,x):
		#shape.__init__(self,x,x)
		self.x = x
		self.y = x
#mysquare = square(10)
#print mysquare.area()
#print mysquare.perimeter()
class doublesquare(square):
	def __init__(self,y):
		self.x = y
		self.y = 2*y
mydoublesquare = doublesquare(20)
print mydoublesquare.area()
print mydoublesquare.perimeter()
