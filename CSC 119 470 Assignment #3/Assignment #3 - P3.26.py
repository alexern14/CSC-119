#Topic 4
#Assignment 3 P3.26
#Programmer: Alexandra Ernst
#Date: 3/2/2018
#Version: Python 3.4

#############################################################################
# Unit conversion. Write a unit conversion program that asks the users
# from which unit they want to convert (fl. oz, gal, oz, lb, in, ft, mi)
# and to which unit they want to convert (ml, l, g, kg, mm, cm, m, km).
# Reject incompatible conversions (such as gal to km). Ask for the value
# to be converted, then display the result:
#   Convert from? gal
#   Convert to? ml
#   Value? 2.5
#   2.5 gal = 9463.5 ml
#############################################################################

convert_from = input("Convert from (fl. oz, gal, oz, lb, in, ft, mi): ")
convert_to = input("Convert to (ml, l, g, kg, mm, cm, m, km): ")
value = int(input("Value? "))

conversion = 0
if convert_from == "fl. oz":
    if convert_to == "ml":
        conversion = value * 29.5735
    else:
        if convert_to == "l":
            conversion = value * 0.0295735
        else:
            if convert_to == "g":
                print("Cannot convert to those units")
            else:
                if convert_to == "kg":
                    print("Cannot convert to those units")
                else:
                    if convert_to == "mm":
                        print("Cannot convert to those units")
                    else:
                        if convert_to == "cm":
                            print("Cannot convert to those units")
                        else:
                            if convert_to == "m":
                                print("Cannot convert to those units")
                            else:
                                if convert_to == "km":
                                    print("Cannot convert to those units")
else:
    if convert_from == "gal":
        if convert_to == "ml":
            conversion = value * 3785.41
        else:
            if convert_to == "l":
                conversion = value * 3.78541
            else:
                if convert_to == "g":
                    print("Cannot convert to those units")
                else:
                    if convert_to == "kg":
                        print("Cannot convert to those units")
                    else:
                        if convert_to == "mm":
                            print("Cannot convert to those units")
                        else:
                            if convert_to == "cm":
                                print("Cannot convert to those units")
                            else:
                                if convert_to == "m":
                                    print("Cannot convert to those units")
                                else:
                                    if convert_to == "km":
                                        print("Cannot convert to those units")
    else:
        if convert_from == "oz":
            if convert_to == "ml":
                print("Cannot convert to those units")
            else:
                if convert_to == "l":
                    print("Cannot convert to those units")
                else:
                    if convert_to == "g":
                        conversion = value * 28.3495
                    else:
                        if convert_to == "kg":
                            conversion = value * 0.0283495
                        else:
                            if convert_to == "mm":
                                print("Cannot convert to those units")
                            else:
                                if convert_to == "cm":
                                    print("Cannot convert to those units")
                                else:
                                    if convert_to == "m":
                                        print("Cannot convert to those units")
                                    else:
                                        if convert_to == "km":
                                            print("Cannot convert to those units")
        else:
            if convert_from == "lb":
                if convert_to == "ml":
                    print("Cannot convert to those units")
                else:
                    if convert_to == "l":
                        print("Cannot convert to those units")
                    else:
                        if convert_to == "g":
                            conversion = value * 453.592
                        else:
                            if convert_to == "kg":
                                conversion = value * 0.453592
                            else:
                                if convert_to == "mm":
                                    print("Cannot convert to those units")
                                else:
                                    if convert_to == "cm":
                                        print("Cannot convert to those units")
                                    else:
                                        if convert_to == "m":
                                            print("Cannot convert to those units")
                                        else:
                                            if convert_to == "km":
                                                print("Cannot convert to those units")
            else:
                if convert_from == "in":
                    if convert_to == "ml":
                        print("Cannot convert to those units")
                    else:
                        if convert_to == "l":
                            print("Cannot convert to those units")
                        else:
                            if convert_to == "g":
                                print("Cannot convert to those units")
                            else:
                                if convert_to == "kg":
                                    print("Cannot convert to those units")
                                else:
                                    if convert_to == "mm":
                                        conversion = value * 25.4
                                    else:
                                        if convert_to == "cm":
                                            conversion = value * 2.54
                                        else:
                                            if convert_to == "m":
                                                conversion = value * 0.0254
                                            else:
                                                if convert_to == "km":
                                                    conversion = value * 0.0000254
                else:
                    if convert_from == "ft":
                        if convert_to == "ml":
                            print("Cannot convert to those units")
                        else:
                            if convert_to == "l":
                                print("Cannot convert to those units")
                            else:
                                if convert_to == "g":
                                    print("Cannot convert to those units")
                                else:
                                    if convert_to == "kg":
                                        print("Cannot convert to those units")
                                    else:
                                        if convert_to == "mm":
                                            conversion = value * 304.8
                                        else:
                                            if convert_to == "cm":
                                                conversion = value * 30.48
                                            else:
                                                if convert_to == "m":
                                                    conversion = value * 0.3048
                                                else:
                                                    if convert_to == "km":
                                                        conversion = value * 0.0003048
                    else:
                        if convert_from == "mi":
                            if convert_to == "ml":
                                print("Cannot convert to those units")
                            else:
                                if convert_to == "l":
                                    print("Cannot convert to those units")
                                else:
                                    if convert_to == "g":
                                        print("Cannot convert to those units")
                                    else:
                                        if convert_to == "kg":
                                            print("Cannot convert to those units")
                                        else:
                                            if convert_to == "mm":
                                                conversion = value * 1609000
                                            else:
                                                if convert_to == "cm":
                                                    conversion = value * 160934
                                                else:
                                                    if convert_to == "m":
                                                        conversion = value * 1609.34
                                                    else:
                                                        if convert_to == "km":
                                                            conversion = value * 1.60924

print(value, convert_from, "=", conversion, convert_to)