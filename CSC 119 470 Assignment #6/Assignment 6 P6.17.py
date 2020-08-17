#Topic 7
#Assignment 6 P6.17
#Programmer: Alexandra Ernst
#Date: 4/8/2018
#Version: Python 3.4

##############################################################################
# Write a program that generates a sequence of 20 random values between
# 0 and 99 in a list, prints the sequence, sorts it, and prints the sorted
# sequence. Use the list sort method
###############################################################################

#import random
import random


my_randoms=[]
for i in range (20):
    my_randoms.append(random.randrange(0,99))
print (my_randoms)

#sort and reprint
sorted(my_randoms)
print(sorted(my_randoms))

