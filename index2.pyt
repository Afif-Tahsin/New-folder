class Employee():
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("Destructor called")
def create_Obj():
    print('Making object...')
    obj = Employee()
    print("Function end...")
    return obj
print("Calling create_Obj function...")
obj = create_Obj()
print("Program end...")