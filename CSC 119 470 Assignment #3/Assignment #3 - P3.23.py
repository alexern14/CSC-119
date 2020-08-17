#Topic 4
#Assignment 3 P3.23
#Programmer: Alexandra Ernst
#Date: 3/2/2018
#Version: Python 3.4

######################################################################
# The original U.S. income tax of 1913 was quite simple. The tax was
# 1% on the first $50,000
# 2% on the amount over $50,000 up to $75,000
# 3% on the amount over $75,000 up to $100,000
# 4% on the amount over $100,000 up to $250,000
# 5% on the amount over $250,000 up to $500,000
# 6% on the amount over $500,000
# There was no separate schedule for single or married tax payers.
# Write a program that computes the income tax according to this schedule.
############################################################################

#Constant Variables
Rate1 = 0.01
Rate2 = 0.02
Rate3 = 0.03
Rate4 = 0.04
Rate5 = 0.05
Rate6 = 0.06
Rate1_limit = 50000
Rate2_limit = 75000
Rate3_limit = 100000
Rate4_limit = 250000
Rate5_limit = 500000
tax1 = 0
tax2 = 0
tax3 = 0
tax4 = 0
tax5 = 0
tax6 = 0

income = float(input("Enter your income: "))

if income <= Rate1_limit:
    tax1 = Rate1 * income
else:
    if Rate2_limit >= income > Rate1_limit:
        tax1 = Rate1 * Rate1_limit
        tax2 = Rate2 * (income - Rate1_limit)
    else:
        if Rate3_limit >= income > Rate2_limit:
            tax1 = Rate1 * Rate1_limit
            tax2 = Rate2 * 25000
            tax3 = Rate3 * (income - Rate2_limit)
        else:
            if Rate4_limit >= income > Rate3_limit:
                tax1 = Rate1 * Rate1_limit
                tax2 = Rate2 * 25000
                tax3 = Rate3 * 25000
                tax4 = Rate4 * (income - Rate3_limit)
            else:
                if Rate5_limit >= income > Rate4_limit:
                    tax1 = Rate1 * Rate1_limit
                    tax2 = Rate2 * 25000
                    tax3 = Rate3 * 25000
                    tax4 = Rate4 * 150000
                    tax5 = Rate5 * (income - Rate4_limit)
                else:
                    if income > Rate5_limit:
                        tax1 = Rate1 * Rate1_limit
                        tax2 = Rate2 * 25000
                        tax3 = Rate3 * 25000
                        tax4 = Rate4 * 150000
                        tax5 = Rate5 * 250000
                        tax6 = Rate6 * (income - Rate5_limit)

totaltax = tax1+tax2+tax3+tax4+tax5+tax6

print ("Your tax is $%.2f" % totaltax)
