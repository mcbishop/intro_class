print "Should you eat that bacon? (The Game - TM) "
question = raw_input("Do you want to feel like angels are frolicking on your taste buds? Answer with 'y', 'n', or 'yes, but' ")

def bacon(angel):
	if angel == "yes" or angel == "y":
		print "Eat it (the bacon)."
	elif angel == "no" or angel == "n":
		print "Clearly you've never tasted bacon. Eat it."
	elif angel == "yes, but":
		print "Yes,  but you're afraid bacon will kill you? Hmmm..."
		coward = raw_input("Are you a coward?")
		if coward == "yes" or coward == "y":
			print "Bacon will turn you into a true warrior."
		else:
			print "Then eat it. (The bacon.)"



bacon(question)
