#Topic 7
#Assignment 6 P6.27
#Programmer: Alexandra Ernst
#Date: 4/8/2018
#Version: Python 3.4

################################################################################
# A theater seating chart is implemented as a table of ticket prices, like this:
# 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10
# 10 10 20 20 20 20 20 20 10 10
# 10 10 20 20 20 20 20 20 10 10
# 10 10 20 20 20 20 20 20 10 10
# 20 20 30 30 40 40 30 30 20 20
# 20 30 30 40 50 50 40 30 30 20
# 30 40 50 50 50 50 50 50 40 30
# Write a program that prompts users to pick either a seat or a price. Mark sold
# seats by changing the price to 0. When a user specifies a seat, make sure it
# is available. When a user specifies a price, find any seat with that price.
################################################################################

#import random
import random


#Build seating chart
Rows = 9
Columns = 10

counts = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]

for i in range(Rows):
    for j in range(Columns):
        print("%8d" % counts[i][j], end="")

    print()

#Number of tickets left to be sold:
num_tix = 90
while num_tix != 0:

#Determine which buying option they would like
    seat_or_price = input("Would you like to 1) pick your seat or 2) be given a random ticket based on price?")

#Execute buying option 1
    if seat_or_price == "1" :

        for i in range(Rows):
            for j in range(Columns):
                print("%8d" % counts[i][j], end="")

            print()

        i = int(input("Choose a row: "))
        i = i -1
        j = int(input("Choose a column: "))
        j= j-1

        if counts[i][j] == 0:
            print("This seat is taken, please try again")
            i = int(input("Choose a row: "))
            i = i - 1
            j = int(input("Choose a column: "))
            j = j - 1

        if counts[i][j] != 0:
            print("Thank you for your purchase! You owe: $", counts[i][j])
            print("\nYour seat is in row %d and seat %d" % (i+1 , j+1 ))
            counts[i][j] = 0
            num_tix = num_tix -1
            print("There are", num_tix, "tickets left.")

#Execute buying option 2
    elif seat_or_price == "2":

        for i in range(Rows):
            for j in range(Columns):
                print("%8d" % counts[i][j], end="")

            print()

        price = int(input("\nEnter the price(10, 20, 30, 40 or 50): "))

        seatFound = False

        for i in range(len(counts)):
            for j in range(len(counts[0])):
                if counts[i][j] == price and not seatFound:
                    seatFound = True
                    counts[i][j] = 0
                    num_tix = num_tix - 1
                    print("\nYour seat is in row %d and seat %d" % (i + 1, j + 1))
                    print("There are", num_tix, "tickets left.")
