# Task 6

# Write the Task 5 titles to the text file.

# Extras:
# Ask the user to specify the name of the output file that will be saved.
#.......................................................................................................................

import task_5
import subprocess
#------------------------------------------------------

def save_name():
    with open("file_name", "w") as obj:
        subprocess.run('python task_5.py', stdout = obj, text = True)

#----------------------------------------------------------------------------

print(save_name())