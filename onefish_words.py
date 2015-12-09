#Write a program that counts how many times each word appears in a file

with open("one_fish_two_fish.txt") as current_fish:
	fish_text = current_fish.read()
words_list1 = fish_text.replace("\n"," ")
words_list = words_list1.split(' ')


words_dict = {}
def create_word_dictionary(random):	
	for key in random:
		if key in words_dict:
			words_dict[key]+=1
		else:
			words_dict[key]=1
	return words_dict

print create_word_dictionary(words_list)
