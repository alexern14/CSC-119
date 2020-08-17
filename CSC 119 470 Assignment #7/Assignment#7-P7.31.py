#Topic 8
#Assignment 7 P7.31
#Programmer: Alexandra Ernst
#Date: 5/3/2018
#Version: Python 3.4

############################################################################
#A store owner keeps a record of daily cash transactions in a text file.
# Each line contains three items: The invoice number, the cash amount, and
# the letter P if the amount was paid or R if it was received. Items are
# separated by spaces. Write a program that prompts the store owner for the
# amount of cash at the beginning and end of the day, and the name of the
# file. Your program should check whether the actual amount of cash at the
# end of the day equals the expected value.
#############################################################################

#Open and write file
text_file = open("write_it.txt", "w")
text_file.write("invoice number, cash amount, P/R\n")
text_file.write("1, 500, R\n")
text_file.write("2, 50, P\n")
text_file.close()

#text_file = open("write_it.txt", "r")
#print(text_file.read())
#text_file.close()

#Declare variables and inputs
beginning = input("Amount of cash at the beginning of the day:")
endofday = input("Amount of cash at the end of the day:")
infilename = input("What is the name of the input file?")

file = open(infilename , "r")

#Read file
line = file.readline()
line.split(",")
while line != "":
   line = file.readline()

#Calculate total and expected total
total = 0

for line in file:
    if line.isdigit():
        total += int(line)

expected = total

total = int(endofday)

if expected == total:
    print("Your end of the day balance is as expected.")
else:
    if expected > total:
        print("Your end of the day balance is less than expected")
    else:
        if expected < total:
            print("Your end of the day balance is more than expected")