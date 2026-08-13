names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names[2] = "Chuck"
print(names)

a = [True, False, None]
print(a[1:1])
print("Length of a:", len(a))

print(list(range(4)))
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(list(range(len(friends))))
for i in range(len(friends)):
    print("Happy New Year,", friends[i])


#list concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)

some = [1, 9, 2, 8, 3, 7]
print(9 in some)

print(dir(list()))

total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    total += value
    count += 1
average = total / count
print("Average:", average)

#another way to do the same thing
numbers = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    numbers.append(value)
average = sum(numbers) / len(numbers)
print("Average:", average)