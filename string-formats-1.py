

# Write a function called check_for_string. It should have one parameter, input.
# Inside the function, it should check if the parameter is of type string. 
# Modify your function to print [input] is a string! or [input] is not a string.

def check_for_string(input):
	if type(input)==str:
		print "%s is a string!" % input
	elif type(input)==int:
		print "%i is not a string." % input
	elif type(input)==float:
		print"%f is not a string." % input
	elif type(input)==bool:
		print"%r is not a string." % input

check_for_string("test")
check_for_string(5)
check_for_string(True)
check_for_string(45.34)


#Write a function called larger that takes two arguments and returns the value of the larger one. Make sure to preface the function calls with the print statement so you can see the result!
#Below is the version using class math and method max.
#import math
#def larger(num1,num2):
#	max (num1,num2)

def larger(num1,num2):
	if num1>num2:
		return num1
	elif num1<num2:
		return num2
	elif num1==num2:
		print "Numbers are equal. Try calling 'larger' again with two different arguments."
#Call larger with arguments 4, 8.
larger(4,8)
#>8

#Call larger with arguments 234*42, 634*23
larger((234*42),(634*23))
#>14582

#Use larger to find the larger of 3 numbers: 4, 63, 32. 
 larger(4,larger( 63, 32))
 #>
63 

#Write a function called smaller that takes two arguments and returns the value of the smaller one. 
#def smaller(num1,num2):
#	min(num1,num2)

def smaller(num1,num2):
	if num1<num2:
		return num1
	elif num1>num2:
		return num2
	elif num1==num2:
		print "Numbers are equal. Try calling 'smaller' again with two different arguments."

# Make sure to preface the function calls with the print statement so you can see the result!
#Call smaller with arguments 3.14, 6.
#>3.14
#Call smaller with arguments True, False
smaller(True,False)
#>False, probably because False has value of 0
#Use smaller to find the smaller of 3 numbers: 4, 63, 32.
# Hint: You can pass a function call as an argument to another function call.
smaller(4,smaller(63,32))
#>4
