#Topic 6
#Assignment 5 Function 2
#Programmer: Alexandra Ernst
#Date: 4/8/2018
#Version: Python 3.4

#####################################################################################
# 2. Write a Python program to perform the task of temperature conversion from
# Celsius to Fahrenheit. Note that given C as the degree of temperature in Celsius,
# the corresponding degree F in Fahrenheit equals 1.8*C + 32.0. For example 50
# degree Celsius should be 122 degree Fahrenheit.
########################################################################################

#Define the function
def celsius(c):
    f = 1.8*c + 32

    print("If the degree celcius is " ,c,", then the degree fahrenheit is:",f)

#Call the function
celsius(50)
