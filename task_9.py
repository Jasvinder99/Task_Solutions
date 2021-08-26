# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.
#.......................................................................................................................
from typing import List

def binary_search(number_list: List, search_number: int) -> int:
    # if list is not sorted
    number_list.sort()
    low: int = 0
    high: int = len(number_list) - 1
    mid: int = 0

    while low <= high:
        mid = (high + low) // 2

        if number_list[mid] < search_number:
            low = mid + 1

        elif number_list[mid] > search_number:
            high = mid - 1

        else:
            return mid

    return -1

#--------------------------------------------------------------------------------------------------------------------

def search_input() -> [str]:

    user_input_list: List[str] = list(input("Enter the List :").split(" " or ","))
    search_num: int = int(input("Enter the number to search in list :"))
    result: int = binary_search(user_input_list, search_num)

    if result != -1 :
        return ("Element is present at index", str(result))

    else:
        return "Element is not present in list"

#----------------------------------------------------------------------------------------------------------------------

print(search_input())
