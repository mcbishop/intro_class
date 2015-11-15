# Tip Calculator
#Create a file called tip_calculator.py inside of ~/intro_class.
# Write all the code for these exercises inside of the tip_calculator.py file.

#Write a function called calculate_tip that has one parameter: total_bill. calculate_tip should return 20% of the total_bill.

def calculate_tip(total_bill):
	total = float(.2*total_bill)
	return total                                                                    


#Print calculate_tip with the total_bill 42.50. It should return 8.500000. 
#	(Hint: print “%f” % calculate_tip(42.50) )

print "%f" % calculate_tip(42.50)
#Use the statement print "%.2f" % calculate_tip(42.50) 

print "%.2f" % calculate_tip(42.50)


# What does the %.2f do? -- 2 decimal places from 0
# Try %.3f and %.0f to make sure your answer to part i is correct.
print "%.3f" % calculate_tip(42.50)
print "%.0f" % calculate_tip(42.50)

# Calculate two more tips using your function!
print "%.2f" % calculate_tip(200.50)
print "%.2f" % calculate_tip(1000.50)

# Write a function called calculate_tip2 that has two parameters: total_bill and tip_percent. calculate_tip2 should return the total_bill*tip_percent.
def calculate_tip2(total_bill, tip_percent):
	return total_bill * tip_percent

# Print calculate_tip2 with the total_bill 42.50 and the tip_percent .2. It should return 8.500000.

print "%f" % calculate_tip2(42.50,.2)

# Use what you learned from 1b to shorten the output to two decimal places.

print "%.2f" % calculate_tip2(42.50,.2)

# Calculate two more tips using your function!
print "%.2f" % calculate_tip2(130,.2)
print "%.2f" % calculate_tip2(65,.2)

# Write a function called tips_with_friends that has three parameters: total_bill, tip_percent, and num_friends. tips_with_friends should return (total_bill*tip_percent)/num_friends.
def tips_with_friends(total_bill, tip_percent, num_friends):
	return (total_bill*tip_percent)/num_friends

# Print tips_with_friends with total_bill 42.50, tip_percent .2, and num_friends 2. It should return 4.250000.

print "%f" % tips_with_friends(42.50,.2,2)


# Use what you learned from 1b to shorten the output to two decimal places.
print "%.2f" % tips_with_friends(42.50,.2,2)

# Modify the print statement to say: “Each person should pay [amount].” where amount is the total each person needs to pay.
# I'm assuming they're splitting the bill as well as the tip.

print "Each person should pay %.2f" % ((42.5/2)+tips_with_friends(42.50,.2,2))

