# i = 10
# while i>0:
# 	if i == 10:
# 		print i
# 	i = i - 1
# 	if i == 0:
# 		print "Blastoff!"
# 	else:
# 		print i
# fruits=['apples','oranges','bananas']
# index=0
# while index<len(fruits):
# 	print fruits[index]
# 	#print goodies
# 	index = index + 1

# Create a function called sum_nums that takes in a number called num. 
#  sum_nums should add up all of the numbers 
#  from 0 until (but not including) num. 
# # sum_nums should return this sum.


answer = int(raw_input("Give me a whole number."))
def sum_nums(num):
	#we want to add up all the numbers between 0 and num.
	# create a range between 0 and "num"
	# and add these numbers together.
	sum = 0
	i = 0
	while (i <= num):
		sum = sum + i
		i = i + 1
	return sum

print sum_nums(answer)


