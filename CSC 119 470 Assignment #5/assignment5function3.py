#Topic 6
#Assignment 5 Function 3
#Programmer: Alexandra Ernst
#Date: 4/8/2018
#Version: Python 3.4

#####################################################################################
# 3. Continually prompt the user for an integer. Constrain the user’s input to
# integers between 1 and 50,000. You can assume that the user will enter an integer
# and not a string or floating point number. Make sure you have a way of exiting the function.
########################################################################################

#Define the function
def int_input():
    num_str = int(input("Input an integer from 1 to 50,000 (0 terminates):"))

    while num_str != 0:
        num_str = int(input("Input an integer from 1 to 50,000 (0 terminates):"))
        if num_str == 0:
            exit()
        if num_str < 1 or num_str > 50000:
            print("That is not in the range.")
            num_str = input("Input an integer from 1 to 50,000:")

#Call the function
int_input()