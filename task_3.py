# Task 3

# Take two lists, say for example these two:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#   1. Randomly generate two lists to test this
#   2. Write this in one line of Python
#................................................................................................................

import random

#--------------------------------------------------------------------------

def intersection_list():

 print("*-"*25)
 first_list_length = int(input("\nEnter the size for first list : "))
 second_list_length = int(input(" Enter the size for second list : "))

 random_first_list = [random.randrange(1, 100) for i in range(first_list_length)]

 random_second_list = [random.randrange(1, 100) for i in range(second_list_length)]

 print("*-"*25, "\nFirst Random generated list are :", random_first_list)
 print("Second Random generated list :", random_second_list)

 return "The Common Elements are :", list(set(random_first_list) & set(random_second_list))

#-----------------------------------------------------------------------------------------------------------------

print(intersection_list())