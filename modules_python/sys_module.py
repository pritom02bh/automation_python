# sys_module in Python: The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.

# print(sys.version_info)
# print(sys.modules)      # By default, python is importing these modules
# print(sys.path)         # Path

# sys.exit()              # this is a function to Stop python

# print(sys.argv)           # To get command line arguments inside the script.

import sys
usr_str = sys.argv[1]
usr_action = sys.argv[2]

if usr_action == 'lower':
    print(usr_str.lower())
elif usr_action == 'upper':
    print(usr_str.upper())
elif usr_action == 'title':
    print(usr_str.title())
else:
    print("Your Option is Invalid !!!! ")