#Topic 5
#Assignment 4 P4.2
#Programmer: Alexandra Ernst
#Date: 3/2/2018
#Version: Python 3.4

###################################################################
# Write programs that read a sequence of integer inputs and print
# a. The smallest and largest of the inputs
# b. The number of even and odd inputs
# c. Cumulative totals. For example, if the input is 1 7 2 9, the
# program should print 1 8 10 19
# d. All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2,
# the program should print 3 5 6
################################################################################

#Prints the largest of the inputs in the sequence
largest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "":
    value= int(inputStr)
    if value > largest:
        largest = value
    inputStr = input("Enter a value: ")

print("The largest number in the sequence is:", largest)


#Prints the smallest of the inputs in the sequence
smallest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "":
    value= int(inputStr)
    if value < smallest:
        smallest = value
    inputStr = input("Enter a value: ")

print("The smallest number in the sequence is:", smallest)


#Prints the number of even and odd inputs
numbers = list()
even_counter = 0
odd_counter = 0
while(True):
    num = input("Enter a value: ")
    if num == '':
        break
    numbers.append(num)
    if int(num)%2 ==0:
        even_counter +=1
    else:
        odd_counter +=1

print (numbers)
print ("Number of even numbers: ", even_counter)
print ("Number of odd numbers: ", odd_counter)


#Prints the cumulative totals
num = input("Enter numbers(separated by spaces): ")
list = num.split(" ")

total = 0
for v in list:
    total += int(v)
    print(total)

#Prints all adjacent duplicates
value = int(input("Enter a value: "))
inputStr = int(input("Emter a value: "))
while inputStr != " ":
    previous = value
    value = inputStr
    if value == previous:
        print(value)
    inputStr = input("Enter a value: ")