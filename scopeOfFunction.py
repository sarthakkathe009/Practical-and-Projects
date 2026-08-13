x = 123 #global variable

def demo_local():
    # x = 124  #local variable
    global x      # Used for accessing gobal variable inside function
    print("Inside function:",x)
    x += 4
    # y = 125

demo_local()
print("Outside function:",x)
# print("Printing y outside the function:",y)  # will result "y not define as function execution compeletes after funciton called"