#Topic 3
#Assignment 2 P2.7
#Programmer: Alexandra Ernst
#Date: 2/9/2018
#Version: Python 3.4

#####################################################################
# Write a program that prompts the user for a radius and then prints
#   the area and circumference of a circle with that radius
#   the volume and surface area of a sphere with that radius
######################################################################

#import math
from math import *

#inputs
radius = int(input("Radius: "))

#calculations
area = pi * radius**2
circ = 2 * pi * radius
volume = (4/3)*pi*(radius)**3
surf_area = 4 * pi * (radius)**2

####################################################################

print("The area of a circle with radius",radius, "is: ",area)
print("The circumference of a circle with radius",radius, "is: ",circ)
print("The volume of a sphere with radius",radius,"is: ",volume)
print("The surface area of a sphere with radius",radius,"is: ",surf_area)

