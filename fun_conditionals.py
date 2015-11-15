
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