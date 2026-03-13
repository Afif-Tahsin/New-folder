class IOString():
    def __init__(self):
        self.str1 = ""
    def getString(self):
        self.str1 = input("Enter String:")
    def print_string(self):
        print(f"Result is: {self.str1.upper()}")
str1 = IOString()
str1.getString()
str1.print_string()