#!/usr/bin/python
#display the options
import calculator_opr
def main():
	import os
	os.system('clear')
	string = "CALCULATOR"
	print string.center(50,"#")
	global choice
	choice = input("\t\t1.Simple Calculator\n\t\t2.Scientific Calculator\n\t\t3.EXIT")
main()
while True:
	if(choice == 1):
		print "\t\t\tSIMPLE CALCULATOR\n\n"
		operation = input("\t1.add\n\t2.sub\n\t3.mul\n\t4.div\n\t5.go back")
		if(operation == 1):
			print"Give two numbers"
			num1 = input("Enter the number1")
			num2 = input("Enter the number2")
			from calculator_opr import add
			print"result of sum ",add(num1,num2)
		if(operation == 2):
			print"Give two numbers"
			num1 = input("Enter the number1")
			num2 = input("Enter the number2")
			print"result of sub ",calculator_opr.sub(num1,num2)
		if(operation == 3):
			print"Give two numbers"
			num1 = input("Enter the number1")
			num2 = input("Enter the number2")
			print"result of mul ",calculator_opr.mul(num1,num2)
		if(operation == 4):
			print"Give two numbers"
			num1 = input("Enter the number1")
			num2 = input("Enter the number2")
			print"result of div ",calculator_opr.div(num1,num2)
		if(operation == 5):
			calculator_opr.go_back()
	elif(choice == 2):
		print "\t\t\t\tSCIENTIFIC CALCULATOR\n\n"
		operation = input("\n\t1.sin\n\t2.cos\n\t3.sqrt\n\t4.powerof\n\t5.go back")
		if(operation == 1):
			number = input("Enter the number in degrees")
			print"result of sin function ",calculator_opr.sin(number)
		if(operation == 2):
			number = input("Enter the number in degrees")
			print"result of cos function ",calculator_opr.cos(number)
		if(operation == 3):
			number = input("Enter the number")
			print"result of square root ",calculator_opr.sqrt(number)
		if(operation == 4):
			print"Give two numbers"
			num1 = input("Enter the number1")
			num2 = input("Enter the number2")
			print"result of power of number ",calculator_opr.power_of(num1,num2)
		if(operation == 5):
			import pdb
			pdb.set_trace()
			calculator_opr.go_back()
	elif(choice == 3):
		exit()
	else:
		print "invalid operation"
