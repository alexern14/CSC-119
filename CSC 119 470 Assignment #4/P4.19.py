#Topic 5
#Assignment 4 P4.19
#Programmer: Alexandra Ernst
#Date: 3/2/2018
#Version: Python 3.4

#############################################################
# Modify the examaverages.py program from worked example 4.1
# so it will also compute the overall average exam grade.
###############################################################

numStudents = int(input("How many students are there? "))
numExams = int(input("How many exam grades does each student have? "))


studentCounter = 0
grandTotal = 0
overallAverage = 0

while studentCounter < numStudents :
    print ("Enter the exam grades for student # ", studentCounter + 1)
    total = 0
    for i in range (1, numExams + 1):
        score = int(input("Exam %d: " % i))
        total = total + score

    average = total / numExams
    print("This student's average is %.2f" % average)

    studentCounter = studentCounter + 1
    grandTotal = grandTotal + total

studentCounter == numStudents
overallAverage = grandTotal/(numStudents*numExams)

print("The total average of all students on all tests was ", overallAverage)
