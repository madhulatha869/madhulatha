#!/usr/bin/python
if(1):
	class Employee():
		empcount = 0
		def __init__(self,salary):
			Employee.empcount += 1
			self.salary = salary
		def displaycount(self):
			return Employee.empcount
		def displaysalary(self):
			return self.salary
		@staticmethod
		def static_fun():
			print "static method"
			print Employee.empcount
	emp1 = Employee(40000)
	print emp1.displaycount()
	print emp1.displaysalary()
	emp2 = Employee(50000)
	print emp2.displaycount()
	print emp2.displaysalary()
	print emp1.displaysalary()
	Employee.static_fun()
if(0):	
	class Number():
		def __init__(self,start):
			self.data = start
		def __sub__(self,other):
			return Number(self.data - other)
		def __mul__(self,other):
			return Number(self.data * other)
		def displaydata(self):
			return self.data
	x = Number(7)
	z = x * 4
	y = x - 4
	print y.displaydata()
	print z.displaydata()
