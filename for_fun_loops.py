# for i in range(1,21):
#     if i != 13:
#         print i
#     elif i == 13:
#         print "hello"
  
# for i in range(10,-1,-1):
#     if i != 0:
#         print i
#     else:
#         print "Blastoff!"

# fruits = ["apples", "oranges", "bananas"]

# for fruit in fruits:
#     print fruit

# for i in range(3):
#     print fruits[i]

# for i in range(len(fruits)):
#     print fruits[i]

#Write a function called sum_nums2 that checks if the parameter num is negative. 
#If it is, sum_nums2 should add up all of the numbers from 0 to the negative number 
#and return that sum. If the parameter num is positive, sum_nums2 should work the 
#same as sum_nums from #7 part A.

def sum_nums(num):
    sum_range = range(0,num+1)
    total = 0 
    for i in sum_range:
        total = total + i
    print total

# sum_nums(5)
# sum_nums(3)

def sum_nums2(num):
    if num < 0:
        total = 0
        sum_range = range(0,num-1,-1)
        print sum_range
        for i in sum_range:
            total = total + i
        print total
    else:
        sum_nums(num)

sum_nums2(-5)
sum_nums2(5)




def FizzBuzz():
    total = range(1,101,1)
    for i in total:
        if ((i % 3 == 0) and (i % 5 == 0)):
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i
FizzBuzz()
