# Here are a couple Practice Problems for you to work on after your class exercises.  this is a primarily a thinking exercise. Write down the steps or methods you think it would take the solve the problem. 


# For each problem, create a function that meets the objective.

# 1.     takes an integer value and returns True if k is even, and  False otherwise.  However, your function cannot use the multiplication, modulo,
# or division operators 

# 2.     takes two integer values and returns True if n  is a multiple of m ,that is, n=mi for some integer I and False otherwise 

# 3.     takes a sequence  of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two.  Do not use the built-in functions min or max in implementing your solution

# 4.     Write a function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n

# Stretch Goal:
# If you want to test your "recipe" of problem solving steps, feel free to use any language you're currently comfortable with (blockly, scratch, snap!, python, javascript, ruby etc)

# in binary numbers, last char of 1 is going to be False/Odd, 0 will be Even/True. Grab last char and use that to determine Odd/Even.
number = int(raw_input("Give me an integer."))
print "your number is: ", number
#convert raw input number to a binary 
print '{0:08b}'.format(number)
#typecast into string 
binumber = '{0:08b}'.format(number)
#grab last character which will indicate 1(odd)/0(even), and then convert to int 
answer = bool(int(binumber[-1]))
#example: binary strong of integer 8 will be '1000' which whill bool 'False' 
# and we want to get '0' to indicate True even
#since binary is 0/True/even and bool is 0/false, I used an if statement to fix.
print "your bool answer is: ", answer
if answer == False:
	print "Number is even."
elif answer == True:
	print "Number is odd."
else:
	print "Not a valid entry."
