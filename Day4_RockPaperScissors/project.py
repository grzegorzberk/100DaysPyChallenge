import random

rock_asci = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_asci = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors_asci = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

icons_rps = [rock_asci, paper_asci, scissors_asci]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer = random.randint(0,2)

if player < 3:
    print(icons_rps[player])
else:
    print("Error, you typed wrong number. Please try again")
    exit(1)

print("Computer choice:\n")
print(icons_rps[computer])

if player == 0 and computer == 0:
    print("Tie")
if player == 0 and computer == 1:
    print("You lose")
if player == 0 and computer == 2:
    print("You win")
if player == 1 and computer == 0:
    print("You win")
if player == 1 and computer == 1:
    print("Tie")
if player == 1  and computer == 2:
    print("You lose")
if player == 2 and computer == 0:
    print("You lose")
if player == 2 and computer == 1:
    print("You win")
if player == 2 and computer == 2:
    print("Tie")