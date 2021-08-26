# Task 7

# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
#.......................................................................................................................

import random
import typing

#-------------------------------------------

def password_generator() -> [str]:

    characters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=`~!@#$%^&*()_+[]{}\|;':,./<>?"
    password_length: int = int(input("\nEnter the Length for password,for example 4,5,9 ..etc"))
    password: str = ""

    for number in range(0, password_length):

        password_character = random.choice(characters)
        password = password + password_character

    return password


#----------------------------------------------------------------------------------------

if __name__ == '__main__' :

    print("\n *:*:*:*:*    Welcome to Password Generator    *:*:*:*:*\n")

    print(password_generator())

    while True :

        generate_again: str = input("\nDo you want to Generate new Password again ..? y/n")

        if generate_again == "y" :

            print(password_generator())

        else:

            exit()
