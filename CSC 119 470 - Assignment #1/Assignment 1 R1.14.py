#Topic 2
#Programmer: Alexandra Ernst
#Date: February 5, 2018
#Version: Python 3.4

#####################################################################
# In order to estimate the cost of painting a house, a painter needs
# to know the surface area of the exterior. Develop an algorithm
# for computing that value. Your inputs are the width, length, and
# height of the house, the number of windows and doors, and their
# dimensions.
#####################################################################

width = int(input("Width of House: "))
length = int(input("Lenth of House: "))
height = int(input("Height of House: "))
surf_area = int((width * height) + (length * height)) * 2

door_number = int(input("How many doors on this house?"))
total_door_volume = int(0)

#this loop calculates total door volume and stores it in int(total_door_volume)
x=0
while x < door_number :
	door_height = int(input("How tall is this door?"))
	door_width = int(input("How wide is this door?"))
	door_volume = int(door_height * door_width)
	total_door_volume = total_door_volume + door_volume
	#print (total_door_volume)
	x = x + 1

window_number = int(input("How many windows on this house?"))
total_window_volume = int(0)

#this loop calculates total window volume and stores it in int(total_window_volume)
x=0
while x < window_number :
	window_height = int(input("How tall is this window?"))
	window_width = int(input("How wide is this window?"))
	window_volume = int(window_height * window_width)
	total_window_volume = total_window_volume + window_volume
	#print (total_window_volume)
	x= x + 1

doors_and_window_volume = int(total_door_volume + total_window_volume)
paintable_surface_area = int(surf_area - doors_and_window_volume)
######################################################################

print ("The total paintable surface area of this house is: ", paintable_surface_area)
