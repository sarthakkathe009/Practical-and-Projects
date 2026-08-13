fhand = open('test_file.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = []
# for k,v in counts.items():
#     newup = (v,k)
#     lst.append(newup)

# lst = sorted(lst,reverse=True)
lst = sorted([(v,k) for k,v in counts.items()],reverse=True) #Using Comprehension

for v,k in lst[:10]:
    print(k,v)