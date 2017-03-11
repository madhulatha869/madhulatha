#!/usr/bin/python
#exp1 check the given number with 100
#and prints the message
if(0):
	num = input()
	if (num > 100):
		print "number is greater than 100"
	elif(num < 100):
		print "number is less than 100"
	else:
		print "number is equals to 100"
#exp2 
if(0):
	i = 1
	while i<11:
		print i
		i += 1
#exp3 print 1 to 5
if(0):
	i = 1
	while i<11:
		print i
		if(i > 4):
			break
		i += 1
#exp4 print 1 to 10 except 5 
if(0):
	i = 1
	while i<11:
		if( i == 5):
			i += 1
			continue
		print i
		i += 1
#exp5 checks the day and print the message
if(1):
	string = raw_input("Enter the day in small letters...")
	if(string == 'monday' or string == 'tuesday' or string == 'wednesday' 
	or string == 'thursday' or string == 'friday'):
		print"Go to office"
	elif(string == 'saturday'or string == 'sunday'):
		print"Enjoy your day"
	else:
		print"invalid day"
