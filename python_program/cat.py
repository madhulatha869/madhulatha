#!/usr/bin/python
import sys
import os
if(0):
	if(len(sys.argv) == 2):
		if(os.path.isfile(sys.argv[1])):
			f1 = open(sys.argv[1],"r")
			print f1.read(),
			f1.close()
		else:
			print "file is not exist"
	else:
		print "give only one file.."
if(0):
	if(len(sys.argv) == 3):
		if(os.path.isfile(sys.argv[1])):
			f1 = open(sys.argv[1],"r")
			f2 = open(sys.argv[2],"w")
			f2 = f1
			print "file2 contains...\n",f2.read(),
			f1.close()
			f2.close()
		else:
			if(os.path.isfile(sys.argv[1])):
				print "file1 is not exist",sys.argv[1]
			else:
				print "file2 is not exits",sys.argv[2]
	else:
		print "give only two files.."
if(1):
	if(len(sys.argv) == 2):
		if(os.path.isfile(sys.argv[1])):
			f1 = open(sys.argv[1],"r")
			print len(f1.read()),
			f1.seek(0)
			print len(f1.read().split()),
			f1.seek(0)
			f1.join(0)
			f1.seek(0)
			print len(f1.readlines())
			f1.close()
		else:
			print "file is not exist"
	else:
		print "give only one file.."
if(0):
	if(len(sys.argv) == 2):
		if(os.path.isfile(sys.argv[1])):
			f1 = open(sys.argv[1],"w+")
			f1.writelines("hi hello\nmadhu\nhow r u")
			f1.seek(0)
			print f1.read()
			f1.close()
		else:
			if(os.path.isfile(sys.argv[1])):
				print "file1 is not exist",sys.argv[1]
			else:
				print "file is not exist"
	else:
		print "give only one file.."

