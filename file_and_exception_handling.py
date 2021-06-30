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
# try:
#     file = open("order.text")
#     print("File found") # Try block required exept or will throw an error
# except FileNotFoundError as errmsg: # errmsg is an Alias ( same as a nick name)
#     print(f"Panic, File not found{errmsg}")
#     # RAISE:  this would print original error message
# finally: # Will run regardless of try and axcept block
#     print("Thank you, see you again")


# ### **Crating a file named order.text. The name must be the same**


# - Let's apply DRY - OOP - Python package
# - if you have completed reading task, please move onto writing/adding items to order.text

# def finding_file(file):
#
#     try:
#         file_name = open(f"{file}.text")
#         print("File found")
#     except FileNotFoundError as errmsg:
#         print(f"Panic, File not found{errmsg}")
#     finally:
#         print("Thank you, see you again")
#
# file = input("What is the name of the file you would like to read?: ").strip()
# print(finding_file(file))

# -------------------------------------------------------------------------
# - Open file and read it

def open_using_with_and_print(file): # Calling the function
# with open(file, "r") as file
    try:
        file_name = open(f"{file}.text", "r")
        print(f"This is your order: ", file_name.read())

        change_item = input("Would you like to change anything? yes/no: ").lower().strip()

        if change_item == "yes":
            add_or_replace_item = input("Would you like to ADD a new order or REPLACE an order or BOTH?: ").lower().strip()
            if add_or_replace_item == 'add':
                return
            elif add_or_replace_item == 'replace':
                return
            elif add_or_replace_item == "both":
                return


        else:
            print("Perfect, thank you")



    except FileNotFoundError as errmsg:
        print(f"Panic, Your order is lost{errmsg}")

    finally:
        print("Thank you, see you again")


file = input("What is the name of the file you would like to read?: ").strip()
print(open_using_with_and_print(file))
