#write a program to count how many times each letter appears in your full name.

name = raw_input("Give me your full name.")
name_dict = {}
def count_letters(name):
	for char in name:
		if char in name_dict:
			name_dict[char]+=1
		else:
			name_dict[char]=1
	return name_dict


print count_letters(name)

# print name_dict.items() 

		#add each letter to a dictionary as a key
		#then add 1 to value if key appears again
