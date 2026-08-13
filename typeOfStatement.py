#Conditional Statements
try:
    x = int(input("Enter a number: "))
    if x < 5:
        print("Hi")
    if x > 10:
        print("Hello")

    print("Bye")

except ValueError:
    print("Invalid input. Please enter a number.")

#Iterative Statements
print("Ready for launch in")
n = 5
while n > 0:
    print(n)
    n -= 1
print("Liftoff!")


#Combination of Constructs

total = 1

print("Enter positive numbers to add to the total")
print("Type a negative number to finish.\n")

while True:
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            print("\nDone")
            break
        total += num
        print(f"Current total: {total}\n")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nFinal total: ", total)
