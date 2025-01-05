import random

print("Welcome to the Number Guessing Game")
print("I'm thinking about number between 1 and 100.")
RAND_NUM = random.randrange(1, 100)

level = input("Choose a difficulty. Type 'easy' or 'hard':   ")
repeat = 0

if level == "easy":
    repeat = 10
elif level == "hard":
    repeat = 5


for i in reversed(range(repeat+1)):
    print(f"You have {i} more attemps to guess")
    if i == 0:
        print(f"Game over, number to guess was {RAND_NUM}!")
    guess = int(input("Make a guess: "))
    if guess < RAND_NUM:
        print("Too low")
    elif guess > RAND_NUM:
        print("Too high")
    elif guess == RAND_NUM:
        print("Bingo!")
        break
