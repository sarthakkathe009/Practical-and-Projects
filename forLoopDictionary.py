jjj = {'chuck': 1, 'annie': 42, 'jan': 100}
print(list(jjj))

print("Keys:", list(jjj.keys()))
print("Values:", list(jjj.values()))
print("Items:", list(jjj.items()))

for key, value in jjj.items():
    print(key, value)

name = input("Enter a file name: ")
handle = open(name, 'r', encoding='utf-8', errors='replace')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
