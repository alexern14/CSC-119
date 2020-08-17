#Topic 6
#Assignment 5 Function 1
#Programmer: Alexandra Ernst
#Date: 4/8/2018
#Version: Python 3.4

#####################################################################################
# 1. Write a function that takes 5 int arguments and returns the largest of the 5.
########################################################################################

#Define the function
def values(*a):
    max = a[0]
    for num in a[1:]:
        if num > max:
            max = num

    print("The largest of all the values is:", max)

#Call the function
values(3, 5, 4, 7, 1)
