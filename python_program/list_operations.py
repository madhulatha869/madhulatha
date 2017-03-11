#!/usr/bin/python
#print the whole list
list1 = [10,20,'hii','madhu',"100"]
if(0):
	print list1
#print element by element in list
if(0):
	for element in list1:
		print element
#insert 30 at the beginning of list
if(0):
	list1.insert(0,30)
	print list1
#insert 40 at the position 1  of list
if(0):
	list1.insert(1,40)
	print list1
#insert at the end
if(0):
	list1.append(50)
	print list1
#delete ele at pos 1
if(0):
	list1.pop(1)
	print list1
#del ele at pos 1 and print the deleted item
if(0):
	num = list1.pop(1)
	print num
#del ele by value
if(1):
	list1.remove('madhu')
	print list1
#print number of elements in the list
if(0):
	num = len(list1)#number of elements in the list
	print num

