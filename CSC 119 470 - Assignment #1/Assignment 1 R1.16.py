#Topic 2
#Programmer: Alexandra Ernst
#Date: 2/5/2018
#Version: 3.4

##################################################################
# You want to find out which fraction of your car's use is for
# commuting to work, and which is for personal use. You know
# the one-way distance from your home to work. For a particular
# period, you recorded the beginning and ending mileage on the
# odometer and the number of work days. Write an algorithm to
# settle this question.
#################################################################

beginning_mileage = int(input("Beginning mileage: "))
ending_mileage = int(input("Ending mileage: "))
work_days = int(input("Number of days worked: "))
one_way_miles_to_work = int(input("Amount of miles to work one-way: "))
total_weekly_miles_traveled = (ending_mileage - beginning_mileage)
print ("Your total weekly miles traveled is: ", total_weekly_miles_traveled)
total_weekly_work_miles = ((one_way_miles_to_work *2)*work_days)
percent_of_miles_worked = total_weekly_work_miles/total_weekly_miles_traveled

########################################################################

print ("The percent of your mileage that went to your work commute is: ", '{:.1%}'.format(percent_of_miles_worked))

print ("The percent of mileage that went to your own personal consumption is: ", '{:.1%}'.format(1-percent_of_miles_worked))


