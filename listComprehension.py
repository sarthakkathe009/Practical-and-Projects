#classical way of creating a list of squares of even numbers from 0 to 20
square_list =[]
for i in range(21):
    if i % 2 == 0:
        square_list.append(i**2)
print(square_list)

#modern way of creating a list of squares of even numbers from 0 to 20 using list comprehension
square_comp = [i**2 for i in range(21) if i % 2 == 0]
print(square_comp)

assert square_list == square_comp
print("Both lists are equal")

words = "Computer Science is the study of computers and computational systems. Unlike electrical and computer engineers, computer scientists deal mostly with software and software systems; this includes their theory, design, development, and application.".split()
initials = [w[0].upper() for w in words if len(w) > 4]
print(initials)

#Map and Filter functions

def double(n):
    return n*2

nums = [1, 2, 3, 4, 5]
doubled_nums = map(double, nums)
print("Original list:", nums)
print("Doubled list:", list(doubled_nums))

def is_even(n):
    return n % 2 == 0

nums = [1, 2, 3, 4, 5]
even_nums = filter(is_even, nums)
print("Original list:", nums)
print("Even numbers:", list(even_nums))

print("Alphabetic strings:", filter(str.isalpha, ['abc', '123', 'a1b2', 'xyz']))