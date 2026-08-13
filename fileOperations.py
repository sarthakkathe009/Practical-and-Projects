fhand = open('mbox-short.txt')
# print(fhand)
# count = 0
# # print(dir(fhand))
# for line in fhand:
#     count += 1
# print("Number of lines in file: ",count)
# inp = fhand.read()
# print(inp)
# print(len(inp))
# print(inp[5:31])

for line in fhand:
    line = line.rstrip() #for fixing the newline character
    if line.startswith('From: '):
        print(line)

try:
    fname = input('Enter filename: ')
    fhand2 = open(fname)
    print(fhand2)
    count = 0
    for line in fhand2:
        count += 1
    print("Number of lines:",count)

except:
    print("File does not found with the name",fname)
    quit()