name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}! You are {age} years old.")

#Type Checking and Safe Conversion
value = input("Enter a number: ")
if value.isdigit():
    number = int(value)
    print(f"Square of the number: {number ** 2}")
else:
    print("Please enter a valid number.")


print('It\'s a nice day')