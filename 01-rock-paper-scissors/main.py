rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
decision = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))

if decision >= 3 or decision <0:
    print("Invalid choice!")
else:
    choices = [rock, paper, scissors]
    computer_choice = random.choice(choices)
    player_choice = choices[decision]
    print(player_choice)
    print(f"computer chose: {computer_choice}")

    if player_choice == rock and computer_choice == paper:
        print("You lost!")
    elif player_choice == rock and computer_choice == scissors:
        print("You won!")
    elif player_choice == paper and computer_choice == scissors:
        print("You lost!")
    elif player_choice == paper and computer_choice == rock:
        print("You won!")
    elif player_choice == scissors and computer_choice == rock:
        print("You lost!")
    elif player_choice == scissors and computer_choice == paper:
        print("You won!")
    else:
        print("Draw!")