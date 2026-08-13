while True:
    line = input("> ")
    if line.lower() == "done":
        break
    print(line)
print("Done!")

while True:
    line = input("> ")
    if line.lower() == "done":
        break
    if line.lower() == "skip":
        continue
    print(line)
print("Done!")

i=1
while i <= 5:
    if i % 2 == 0:
        pass
    else:
        print("Processing", i)
    i += 1