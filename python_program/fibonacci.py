#!/usr/bin/python
#fibonacci series
if(1):
	list1 = [0,1]
	for ele in range(2,101):
		num = list1[len(list1)-2] + list1[len(list1)-1]
		if(num > 100):
			break
		list1.append(num)
print list1
