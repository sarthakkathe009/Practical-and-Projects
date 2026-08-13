num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("The sum of the digits is:", sum)

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number.")