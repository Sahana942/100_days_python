from art import logo, vs
from game_data import data
import random

print(logo)
score=0
continue_game = True
acc_b = random.choice(data)

def format_data(account):
    acc_name = account["name"]
    acc_description = account["description"]
    acc_country = account["country"]
    return f"{acc_name},a {acc_description}, from {acc_country}."

def check_guess(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

while continue_game:

    acc_a=acc_b
    acc_b=random.choice(data)
    while acc_a == acc_b:
        acc_b=random.choice(data)

    print(f"Compare A: {format_data (acc_a)}")
    print(vs)
    print(f"Against B: {format_data (acc_b)}")

    guess = input('Who has more followers? Type "A" or "B":').lower()

    a_follower_count = acc_a["follower_count"]
    b_follower_count = acc_b["follower_count"]

    correct = check_guess(guess, a_follower_count, b_follower_count)

    if correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, thats wrong. Final score: {score}.")