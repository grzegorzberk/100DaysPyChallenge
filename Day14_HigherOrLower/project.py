import random
from game_data import data as data
from art import logo as logo
from art import vs as vs

game_over = False
score = 0

def roll_random_opponent():
    return random.choice(data)

def compare_followers(a, b):
    if a > b:
        return "A"
    elif b > a:
        return "B"

def show_opponent(opponent, data):
    print(f"Compare {opponent}: {data['name']}, a {data['description']}, from {data['country']}")

def end_game(score):
    print("\n" * 20)
    print(logo)
    print(f"Sorry that's wrong. Your score: {score}")


while(game_over!=True):
    print(logo)
    opponent_B = roll_random_opponent()
    opponent_A = roll_random_opponent()

    if score > 0:
        print(f"You're right! Current score: {score}")

    show_opponent("A", opponent_A)
    print(vs)
    show_opponent("B", opponent_B)
    
    user_choice = input("Who has more followers? Type 'A' or 'B':  ")
    correct_answer = compare_followers(opponent_A['follower_count'], opponent_B['follower_count'])
    if user_choice == correct_answer:
        score += 1
        print("\n"*20)
    else:
        game_over = True
        end_game(score)