import random
from art import logo

GAME_MODE_EASY = 10
GAME_MODE_HARD = 5

print(logo)
game_mode = input("Enter Difficulty Level (Easy/Hard):").lower()

"""
This Metod will generate random number to guess
"""


def random_number_generator():
    return (random.choice(range(1, 99)))


gussing_number = random_number_generator()

"""
This Metod compares the user guessed number with actual number
and print the results accordingly
"""


def compute_gussing_number(user_input, gussing_number):
    if user_input == gussing_number:
        print(f"You have Guessed it Correct !!! - {gussing_number}")
        exit()
    elif user_input < gussing_number:
        print("Guessed it Too Low...")
    else:
        print("Guessed it Too High...")


def play_game(game_mode):
    while game_mode >= 1:
        user_input = int(input("Enter Gussing Number between 1 to 99:"))
        compute_gussing_number(user_input, gussing_number)
        game_mode -= 1
        print(f"You have {game_mode} attempts remaining..!!!")
    print("Sorry, you LOOSE....Please try Again...")


if game_mode == "easy":
    play_game(GAME_MODE_EASY)
elif game_mode == "hard":
    play_game(GAME_MODE_HARD)
else:
    print("Enter Valid Choice")
