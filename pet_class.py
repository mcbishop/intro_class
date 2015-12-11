#Turn your pet example into a class and create an instance of that class for your particular pet

class Dog(object):
	def __init__(self, name, color, weight, breed, collar, fur_type, tail):
		self.name = name
		self.color = color 
		self.weight = weight
		self.breed = breed
		self.collar = collar
		self.fur_type = fur_type
		self.tail = tail

	def dog_weight(self, weight):
		if weight <= 30:
			print "This dog is approved for lap snuggling."
		else:
			print "Do not attempt to put this dog in your lap due to potential injury."


Lady = Dog("Lady","fawn",50,"Pit Bull","black fabric","short","uncropped")
Moose = Dog("Moose","fawn",25,"Pug","red","short","curly")
Rags = Dog("Rags","black",10,"Westie/terrier mix","red","medium wirey","shaggy")

#Lady.dog_weight()
Moose.dog_weight(50)
Rags.dog_weight(10)


print Moose.color 
print Lady.tail
