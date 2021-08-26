# Task 10

# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# akita@securitybrigade.com
# Then, the output of the program should be:
# securitybrigade
# In case of input data being supplied to the question, it should be assumed to be a console input.
#.......................................................................................................................
import typing
def get_company_name(url: str) ->[str]:
        return url.split('@')[-1].replace(".com", "")

#------------------------------------------------------------------------------------------------------------------
print(get_company_name(input()))
