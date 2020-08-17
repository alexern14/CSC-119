# Topic 4 - Conditions
# Programmer: Candace Garrod
# Version: 1
# Date: March 1, 2013
#
# Create a dice game that uses two six-sided dice. Each time the program runs, use random
# numbers to assign values to each die variable. Output a "player wins" message to the user if the
# sum of the two dice is 7 or 11. Otherwise output the sum of the two dice and thank the user
# for playing.
#
#
#
##############################################################################################
#
#                                  Declare/Initialize 
#
##############################################################################################
die1 = 0
die2 = 0
response = " "
totaldice = 0
##############################################################################################
#
#                            Determine whether the player would like to play
#
##############################################################################################
print("Would you like to play a dice game? \n")
response = input("Enter a 'y' or 'yes' to play the game: ")
if response == "y" or response == "yes" :print("\nOK, I will roll the dice!")
##############################################################################################
#
#                           Import random - Setup the random generator to roll the dice
#
##############################################################################################
import random
die1 = random.randrange(6)+1
die2 = random.randrange (6) + 1
##############################################################################################
#
#                           Calculate the roll
#
##############################################################################################
totaldice = die1 + die2
print ("\nYour first number is: ", die1)
print ("\nYour second number is: ", die2)
print
print ("\n You rolled a total of:" , totaldice)
if totaldice == 7 or totaldice == 11: print ("\nCongratulations you won!")
else: print ("\nYou lost this one!")
#############################################################################################
#
#                                             End the game
#
#############################################################################################
input("\nPress the Enter to quit this game" )
print ("\nThank you for playing!")

                                    


