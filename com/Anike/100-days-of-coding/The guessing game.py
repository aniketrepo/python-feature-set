import random

print("Welcome to the guessing game!")
rng = int(input("Please enter the range (from 1 to): "))

print(f"Alright! Generating a number between 1 and {rng}!")
to_guess = random.randint(1, rng)

attempts = 0

while True:
    guessed = int(input("Please enter your guess: "))
    attempts += 1
    if guessed > to_guess:
        print("Too high! Try again.")
    elif guessed < to_guess:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        break
print(f"You guessed the correct number in {attempts} attempts.")
