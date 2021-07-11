class ExceptionHandling:
    def __init__(self,file_name):
        self.file_name = file_name
        try:
            open(f"{self.file_name}.text")
            print("File found")
        except FileNotFoundError as errmsg:
            print(f"Panic, File not found{errmsg}")
        finally:
            print("Thank you, see you again")