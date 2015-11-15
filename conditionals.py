# Use the python interpreter to find out if the following boolean expressions are True. If they are False, how would you fix them to make them True?
8 == 8
#True

8 == “8”
#Change to 8 == 8 or "8" == "8"

8 == 8.0
#True

“hi” == “hi”
#True

“HI” == “hi”
#False b/c is case sensitive - change to "HI" == "HI" or "hi" == "hi"

“HI” > “hi”
# False because both evaluate to True. Change to "HI"=="hi" to == True

# Make expressions that evaluate to True using the following operators:
2 == 2
2 != 3
3 > 2
1 < 2
2 >= 1
4 <= 4
# Make expressions that evaluate to False using the following operators:
 ==
!=
>
<
>=
<=
# Use the python interpreter to find out if the following boolean expressions are True.
True == True
False == False
5 == True
5 == False
bool(5) == True
“bye” == True
“bye” == False
bool(“bye”) == True

# Logical Operators
# Use the python interpreter for the following exercises.
# Test if 5 is greater than 9 and less than 3 using logical operators.
3>5>9 #False

# Test if 10 is less than 10 or equal to 10.
10<=10 #True

# Use the not logical operator to see what not 9 is. 
not 9 #False 
# Use the not logical operator to see what not “hello” is. 
not "hello"  #False

# Conditional Statements
# Create a file called conditionals.py inside of ~/intro_class. Write all the code for these exercises inside of the conditionals.py file.
# If your name is greater than your pair’s name, print “My name is greater!”
# Else, if your pair’s name is greater than yours, print “Their name is greater.”
# Else, print “Our names are equal!” 

if "Meg">"Dori":
	print "My name is greater!"
elif "Dori">"Meg":
	print "Their name is greater."
else:
	print "Our names are equal!"



#Write a conditional to test if today’s date is at least halfway through the month. If it is, print “Oh, we’re halfway there!” Otherwise, print “The month is still young.”
#Set a variable called today equal to the day of the week it is.
#If today is Monday, print “Yay class day!”
#Else, if today is Tuesday, print “Sigh, it’s only Tuesday.”
#Else, if today is Wednesday, print “Humpday!”
#Else, if today is Thursday, print “#tbt”
#Else, if today, is Friday, print “TGIF!”
#Else, print “Yeah, it’s the weekend!”

today = "Thursday"

if today == "Monday":
	print "Yay class day!"
elif today == "Tuesday":
	print "Sigh, it's only Tuesday."
elif today == "Wednesday":
	print "Humpday!"
elif today == "Thursday":
	print "#tbt"
elif today == "Friday":
	print "TGIF!"
else:
	print "Yeah, it's the weekend!"
