# Math Calculator
# Create a file called calculator.py inside of ~/intro_class. Write all the code for these exercises inside of the calculator.py file.
# Write a function add that has two parameters num1 and num2. add should return the num1 and num2 added together.

def add(num1,num2):
	return num1 + num2

#Use print add(4,5) to test your function and make sure it prints the right answer.

print add(4,5)
#returned 9

# Write a function subtract that has two parameters num1 and num2.  subtract should return num2 subtracted from num1.

def subtract(num1,num2):
	return num1 - num2

#Test your function and make sure it prints the right answer.

print "%.2f" % subtract(3,2)

# Write a function multiply that has two parameters num1 and num2. multiply should return the num1 and num2 multiplied together.
def multiply(num1,num2):
	return num1*num2

# Test your function and make sure it prints the right answer.
print "%.2f" % multiply(3,2)

# Write a function divide that has two parameters num1 and num2. divide should return num1 divided by num2.
def divide(num1,num2):
	return num1/num2

Test your function and make sure it prints the right answer.

print "%.2f" % divide(1/2)

# Write a function modulo that has two parameters num1 and num2. modulo should return num1 modulo num2.
def modulo(num1,num2):
	return num1 % num2

#Test your function and make sure it prints the right answer.

print "%.2f" % modulo(4,8)

#Write a function power that has two parameters base and exponent. power should raise the base to the exponent power.
#Test your function and make sure it prints the right answer.

def power(base,exponent):
	return base ** exponent

print "%.2f" % power(2,3)

#Write a function square that has one parameter num. square should return num raised to the power of 2.
#Use the function power to calculate the square.

def square(num):
	return power(num,2)

#Test your function and make sure it prints the right answer.

print "%.2f" % square(8) #is correct

#Use your calculator functions to do the following math problems:
	Hint: Break it up into pieces and then put all the pieces together!
#(4+5) + (9-6)
print "%.2f" % add(add(4,5),subtract(9,6))

#(12/2) - 60

print "%.2f" % subtract(divide(12,2),60)

# 1 + 2 + 3
add(add(1,2),3)

#(1 + 2)2
multiply(add(2,3),2)

#(3%4) / 9*9 
divide(modulo(3,4),multiply(9,9)) 

# 7 * (3+8)
multiply(7,add(3,8))

# (1+2) - (3 * (4+5))
subtract(add(1,2),(multiply(3,(add(4,5)))))

# 3(2+3)
multiply(3,(add(2,3)))