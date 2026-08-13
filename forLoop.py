for i in [5,4,3,2,1]:
    print(i)
print("Blastoff!")

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year:", friend)
print("Done!")

for i in range(5):
    print(i)

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)

smallest_so_far = None
print("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("After", smallest_so_far)

names = ["Joseph", "Glenn", "Sally"]
for name in names:
    if name is not "Joseph":
        print("Happy New Year:", name)

largest_so_far = -1

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Before", largest_so_far)

for the_num in numbers:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far)