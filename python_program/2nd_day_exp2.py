#!/usr/bin/python
#printing the values of pi and sin90
if(0):
	import math
	print "pi value is ...",math.pi
	print "sin90 value is...",math.sin(math.radians(90))
#program to clear the screen
if(0):
	import os
	os.system('clear')
#program to print version
if(0):
	import sys
	print sys.version
#program to change the directory
if(0):
	import os
	os.chdir('/home/madhulatha/madhu')
	path = os.getcwd()
	print path
#prime numbers
if(0):
	for num in range(1,101):
		count = 0
		i = 1
		while (num%i == 0):
			count = count + 1
			i = i + 1
		if(count == 2):
			print num
#command line arguments
if(1):
	import sys
	res = int(sys.argv[1]) + int(sys.argv[2])
	print res
