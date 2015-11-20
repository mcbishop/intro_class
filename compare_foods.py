meg_fav_foods = open("meg_fav_foods.txt")
meg_list = meg_fav_foods.readlines()
meg_fav_foods.close()

monique_fave_foods = open("monique_fav_foods.txt")
mo_list = monique_fave_foods.readlines()
monique_fave_foods.close()

# def compare_favs(list1,list2):
# 	if list1[0] == list2[0]:
# 		print "Our favorite foods are the same!"
# 	else:
# 		print "Our favorite foods are different!"


 #compare_favs(meg_list, mo_list)

def compare_favs2(list1, list2):
	if list1[0] == list2[0]:
		print "We both love %s"%(list1[0])
	if list1[1] == list2[1]:
		print "We both love %s"%(list1[1])
	if list1[2] == list2[2]:
		print "We both love %s"%(list1[2]) 



#compare_favs2(meg_list, mo_list)

#for loop version

def compare_favs3(list1,list2):
    for i in list1:
    	for j in list2:
    		if i==j:
    			print "We both love %s"%(i)



compare_favs3(meg_list,mo_list)




