rows = int(input("Enter the number of rows: "))
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

#using for loop
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

rows = 3
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))