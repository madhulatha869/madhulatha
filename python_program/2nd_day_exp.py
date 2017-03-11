#negative index
if(0):
	list1 = [1,2,3,5,8,6]
	for i in range(-6,0,1):
		print list1[i]
#sequences
if(0):
	list1 = [10,20,(3,4)]
	tup1 = (10,20,[4,3])
#	list1[2][0] = 5 we can't modify the element in tuple
	tup1[2][0] = 5
	print tup1[2][0]#we can modify the element in list 
#slicing
if(0):
	tuple1 = (1,2,3,4,5,6,7)
	list1 = [10,20,30,40]	
	tup2 = tuple1[:5]
	print tup2
	tup2 = tuple1[::2]#it slice the indexes of even places
	print tup2		  #print 1,3,5,7 for given tuple1
	list2 = list1[1::2]#it slice the indexes of odd places
	print list2
#dictionary
if(1):
	dict1 = {'details':{'name':['madhu','latha'],'id_no':30869}}
	print dict1
	print dict1.keys()
	print dict1.values()
	print dict1['details']['name'][0]
	print dict1['details']['name'][1]
	print dict1['details']['id_no']
