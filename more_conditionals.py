# def my_name(name1, name2):
# 	if name1 > name2:
# 		print "My name is greater!"
# 	elif name1 < name2:
# 		print "Their name is greater!"
# 	else:
# 		print "Our names are equal!"

# my_name("Monique", "Meg")

# def is_halfway(date):
# 	if int(date) >= 15:
# 		print "Oh, we're halfway there!"
# 	else:
# 		print "The month is still young."

# is_halfway(17)

# today = "Tuesday"

# def today_day(day):
# 	if day == "Monday":
# 		print "Yay class day!"
# 	elif day == "Tuesday":
# 		print "Sigh! It's only Tuesday!"
# 	elif day == "Wednesday":
# 		print "Humpday!"
# 	elif day == "Thursday":
# 		print "#tbt"
# 	elif day == "Friday":
# 		print "TGIF!"
# 	else:
# 		print "Yeah, it's the weekend!"

# today_day(today)

#Write a function called check_for_string.


# def check_for_string(input):
# 	if type(input) == str:
# 		print "%s is a string!" % input
# 	else:
# 		print "%r is not a string." % input 

# check_for_string(True)
# check_for_string(2876)
# check_for_string("String")

# def bar(age):
# 	if (age >= 21):
# 		print "I can go to a bar."
# 	elif (21 > age >= 18):
# 		print "I can vote but I cannot go to a bar."
# 	else:
# 		print "I cannot vote or go to a bar, but I can go to an all-ages club."

# bar(17)
# bar(21)

def even(num):
	if num % 2 == 0:
		return True
	else:
		return False

# odd(7)
# odd(8)

if even(8) and even(9):
	print "Both numbers are even."
elif (even(8) == True) and (even(9)== False):
	print "8 is even and 9 is odd."
elif (even(8) == False) and (even(9) == True):
	print "8 is odd and 9 is even."
else:
	print "Both numbers are odd! Check all of math because it failed."


def fav_color(color):
	if (color == "blue") or (color == "yellow") or (color == "red"):
		print "My fav color is primary color!"
	else:
		print "My favorite color is a secondary color, but it is just as important as a primary color."

fav_color("pantone shade #4982")
