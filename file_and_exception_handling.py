# - Playing arounf with different errors

# print (0/0) # ZeroDivisionError: division by zero
#
# num = 9 # SyntaxError: invalid syntax
# if num > 8
#     print(num)


# ### Create a file with required permission and see what errors/ assumptoipns are possible to be seen

# file = open("order.text") # open() takes a string arg with file name

# print(file) # ERROR: FileNotFoundError: [Errno 2] No such file or directory: 'order.text'


# - Second iteration
try:
    file = open("order.text")
    print("File found") # Try block required exept or will throw an error
except FileNotFoundError as errmsg: # errmsg is an Alias ( same as a nick name)
    print(f"Panic, File not found{errmsg}")
    # RAISE:  this would print original error message
finally: # Will run regardless of try and axcept block
    print("Thank you, see you again")


# ### **Crating a file named order.text. The name must be the same**


# - Let's apply DRY - OOP - Python package