# Number Guessing Game
print("Guess the number between 1 to 10")
secret = 7
guess = int(input("Enter your guess: "))
if guess == secret:
    print("You Won!")
else:
    print("Wrong! The number was", secret)
