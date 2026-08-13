def banner(text: str):
    print("=" * (len(text) + 4))
    print(f"  {text}")
    print("=" * (len(text) + 4))

fruit = 'banana'
index = 0
while index < len(fruit):
    letters = fruit[index]
    print(index,letters)
    index += 1

banner("Using for loop")
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1
    print(letter)
print("a occurred in fruit: ",count)
