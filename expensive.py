# Given a dictionary of items and their prices, write a program that returns the most expensive 
#item.

prices = {"banana":4,"apple":5,"orange":1.5,"pear":3}

# look at value of each item. Compare it to the next. Pick the largest item and compare it to the next. Continue until no more items exist and print the largest item.

fruit = ""
biggest = 0

for x in prices: 
	cost = prices[x] #grabs value of each item
	if cost > biggest:
		biggest = cost
		fruit = x 
print fruit, biggest
