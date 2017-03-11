#!/usr/bin/python
class A():
	def __init__(self,i):
		self.i = 100
class B():
	def __init__(self,j):
		self.j = 200
class c(A,B):
	def __init__(self,i):
		A.__init__(self,i)
		B.__init__(self,k)
		#self.i = k
		#self.j = k
		self.k = 300
class_c = c(500)
print class_c.i
print class_c.j
print class_c.k
