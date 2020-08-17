#Topic 3
#Assignment 2 P2.6
#Programmer: Alexandra Ernst
#Date: 2/9/2018
#Version: Python 3.4

################################################################
# Write a program that prompts the user for a measurement in
# meters and then convert it to miles, feet, and inches.
###############################################################

#Inputs
meter_measurement = int(input("A measurement in meters: "))

#Conversion factor
conversion_factor = float(0.000621371)

#Calculations
miles = meter_measurement * conversion_factor
feet = miles * 5280
inches = feet * 12

##############################################################

print("Your measurement in miles: ", miles)
print("Your measurement in feet: ", feet)
print("Your measurement in inches: ", inches)