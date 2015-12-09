#write a program that counts how many times each word appears in a random string

#add word to a giant string
words = raw_input("Give me a sentence.")
# print words 
#split the string by spacebar so that each word is a list item
words_list = words.split(' ')
# print words_list

#take the split item and turn it into a dictionary 
words_dict = {}
def create_word_dictionary(random):	
	for key in random:
		if key in words_dict:
			words_dict[key]+=1
		else:
			words_dict[key]=1
	return words_dict

print create_word_dictionary(words_list)


