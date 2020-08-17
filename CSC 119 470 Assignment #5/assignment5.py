#Topic 6
#Assignment 5
#Programmer: Alexandra Ernst
#Date: 4/8/2018
#Version: Python 3.4

#####################################################################################
# Combine the following 4 functions into one program with a main driver:
# 1. Write a function that takes 5 int arguments and returns the largest of the 5.
#
# 2. Write a Python program to perform the task of temperature conversion from
# Celsius to Fahrenheit. Note that given C as the degree of temperature in Celsius,
# the corresponding degree F in Fahrenheit equals 1.8*C + 32.0. For example 50
# degree Celsius should be 122 degree Fahrenheit.
#
# 3. Continually prompt the user for an integer. Constrain the user’s input to
# integers between 1 and 50,000. You can assume that the user will enter an integer
# and not a string or floating point number. Make sure you have a way of exiting the function.
#
# 4. Write a function that calculates that computes the balance of a bank account
# with a given initial balance and interest rate, after a given number of years.
# Assume interest is compounded yearly.
########################################################################################

#Define the functions
#
#Function that takes 5 integers and returns the largest of the 5
def values(*a):
    max = a[0]
    for num in a[1:]:
        if num > max:
            max = num

    print("The largest of all the values is:", max)

#converts degrees C to degrees F
def celsius(c):
    f = 1.8*c + 32

    print("If the degree celcius is " ,c,", then the degree fahrenheit is:",f)

#prompts for an integer between 1 and 50,000
#if not in that range, ask for another integer
#0 to exit the program
def int_input():
    num_str = int(input("Input an integer from 1 to 50,000 (0 terminates):"))

    while num_str != 0:
        num_str = int(input("Input an integer from 1 to 50,000 (0 terminates):"))
        if num_str == 0:
            exit()
        if num_str < 1 or num_str > 50000:
            print("That is not in the range.")
            num_str = input("Input an integer from 1 to 50,000:")

#calculates the balance of a bank account with a given balance, interest rate, and years.
#interest is compounded yearly
def main():
    balance = float(input("Balance: $ "))
    intRate = float(input("Interest Rate (%) : "))
    years = int(input("Years: "))
    newBalance = calcBalance(balance, intRate, years)

    print ("New baance:  $%.2f"  %(newBalance))

def calcBalance(bal, int, yrs):
    newBal = bal
    for i in range(yrs):
        newBal = newBal + newBal * int/100
    return newBal

#Main Driver
#Call each function to run
values(1,8,3,6,2)
celsius(50)
main()
int_input()
