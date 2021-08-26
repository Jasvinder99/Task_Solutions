
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

#......................................................................................................................

'''
# Solutuion_1:
def first_last_list():
    number_list=list(input("Enter the Number List...").split(" " or ","))
    return [number_list[0],number_list[-1]]

print(first_last_element())
'''
#------------------------------------------------------------------------------------
# Solution 2:
from typing import List

def first_last_element() -> [List]:
    #number_list: list = []
    print("\n")

    try:
        number_list = list(input("Enter the number list :").split(" " or ","))

    except ValueError:
        print("Please enter valid Number list:")

    else:

        return [ number_list[0], number_list[-1] ]

#-------------------------------------------------------------------------------------------------------

print(first_last_element())
