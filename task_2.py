# Task 2

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele
# Then I would see the string:
#  Michele is name My
# shown back to me.
#.......................................................................................................................
from typing import List

def reverse_words(long_string: str) -> str:
    words: List[str] = long_string.split(" ")

    return " ".join(words[::-1])

#-----------------------------------------------------------------------------------------------

print(reverse_words(input("\n Enter the  long String :")))
