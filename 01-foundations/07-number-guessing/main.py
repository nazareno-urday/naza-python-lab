def create_list():
    for i in range(1,101):
        numbers.append(i)

def compare(guess, choice):
    global lives

    if guess < choice:
        print("Too low!")
        lives -= 1

    elif guess > choice:
        print("Too high!")
        lives -= 1

import random

numbers = []
create_list()
in_game = True
lives = 0

print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

choice = random.choice(numbers)

while in_game:

    if lives == 0:
        in_game = False
        break

    print(f"You have {lives} attemps remaining to guess the number.")
    guess = int(input("Guess the number: "))

    if choice == guess:
        print("You got it!")
        in_game = False

    else:
        compare(guess, choice)