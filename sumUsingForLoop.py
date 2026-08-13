zork = 0
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

count = 0
sum = 0
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, round(sum/count, 2))

#Filtering Loop
print('Before')
for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number', value)
print('After')

#Searching Loop
found = False
print('Before')
for value in [9,41,12,3,74,15]:
    if value == 3:
        print('Found', value)
    print('Current number', value)
print('After',found)