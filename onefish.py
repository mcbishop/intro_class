#write a program that counts how many times each letter appears in a file. return a dictionary.

#open_fish= open("one_fish_two_fish.txt")

fish_diction = {}

with open("one_fish_two_fish.txt") as current_fish:
	fish_text = current_fish.read()

	def count_letters(fish):
		for char in fish:
			if char in fish_diction:
				fish_diction[char]+=1
			else:
				fish_diction[char]=1
		return fish_diction


print count_letters(fish_text)
