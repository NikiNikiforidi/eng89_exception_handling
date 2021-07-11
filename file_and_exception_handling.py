# - Playing around with different errors

# print (0/0) # ZeroDivisionError: division by zero
#
# num = 9 # SyntaxError: invalid syntax
# if num > 8
#     print(num)


# ### Create a file with required permission and see what errors/ assumptoipns are possible to be seen

# file = open("order.text") # open() takes a string arg with file name

# print(file) # ERROR: FileNotFoundError: [Errno 2] No such file or directory: 'order.text'


# - Second iteration
# try:
#     file = open("order.text")
#     print("File found (try, runs if file exists)") # Try block required except or will throw a file not found error
# except FileNotFoundError as errmsg: # errmsg is an Alias (same as a nick name)
#     print(f"Panic, File not found{errmsg} (except, runs if file doesn't exist)")
#     # RAISE:  this would print original error message
# finally: # Will run regardless of try and except block
#     print("Thank you, see you again ( runs regardless) ")


# ### **Creating a file named order.text. The name must be the same as in the code**


# - Let's apply DRY - OOP - Python package
# - if you have completed reading task, please move onto writing/adding items to order.text

# 1) Create a class with methods
# 2) Create a package, and import class with inheritance


# - Created a package and put the exception handling class in the app directory, in a file called `exception_handlong.py`
# Created a file called `__init__.py` in app directory
# Created a file ( same directory as app) called `program.py`


# -------------------------------------------------------------------------
# - Open file and read it
#
# def open_using_with_and_print(file): # Calling the function
# # with open(file, "r") as file
#     try:
#         file_name = open(f"{file}.text", "r")
#         print(f"This is your order: ", file_name.read())
#
#         change_item = input("Would you like to change anything? yes/no: ").lower().strip()
#
#         if change_item == "yes":
#             add_or_replace_item = input("Would you like to ADD a new order or REPLACE an order or BOTH?: ").lower().strip()
#             if add_or_replace_item == 'add':
#                 return
#             elif add_or_replace_item == 'replace':
#                 return
#             elif add_or_replace_item == "both":
#                 return
#
#
#         else:
#             print("Perfect, thank you")
#
#
#
#     except FileNotFoundError as errmsg:
#         print(f"Panic, Your order is lost{errmsg}")
#
#     finally:
#         print("Thank you, see you again")
#
#
# file = input("What is the name of the file you would like to read?: ").strip()
# print(open_using_with_and_print(file))
