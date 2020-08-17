#Topic 5
#Assignment 4 P4.19
#Programmer: Alexandra Ernst
#Date: 3/2/2018
#Version: Python 3.4

#############################################################
# Modify the examaverages.py program from worked example 4.1
# so it will also compute the overall average exam grade.
###############################################################

numExams = int(input("How many exam grades does each student have? "))
numStudents = int(input("How many students are there? "))

moregrades = "Y"

while moregrades == "Y" :
    print ("Enter the exam grades. ")
    total = 0
    for i in range (1, numExams + 1):
        score = int(input("Exam %d: " % i))
        total = total + score

    average = total / numExams
    print("The average is %.2f" % average)

    moregrades = input("Enter exam grades for another student (Y/N)? ")
    moregrades = moregrades.upper()

while moregrades == "N":



    print("The overall average is %.2f" % overall_average)
