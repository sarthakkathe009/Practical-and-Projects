cabinet = dict()
cabinet['apple'] = 10
cabinet['banana'] = 5
cabinet['orange'] = 8
print(cabinet)

# counts = dict()
# names=['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
# for name in names:
#     # if name not in counts:
#     #     counts[name] = 1
#     # else:
#     #     counts[name] += 1/
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

counts = dict()
print("Enter a line of text")
line = input('> ')

words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)