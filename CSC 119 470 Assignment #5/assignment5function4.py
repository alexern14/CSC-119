#Topic 6
#Assignment 5 Function 4
#Programmer: Alexandra Ernst
#Date: 4/8/2018
#Version: Python 3.4

#####################################################################################
# 4. Write a function that calculates that computes the balance of a bank account
# with a given initial balance and interest rate, after a given number of years.
# Assume interest is compounded yearly.
########################################################################################

#Define the function
def main():
    balance = float(input("Balance: $ "))
    intRate = float(input("Interest Rate (%) : "))
    years = int(input("Years: "))
    newBalance = calcBalance(balance, intRate, years)

    print ("New balance:  $%.2f"  %(newBalance))

def calcBalance(bal, int, yrs):
    newBal = bal
    for i in range(yrs):
        newBal = newBal + newBal * int/100
    return newBal

#Call the function
main()