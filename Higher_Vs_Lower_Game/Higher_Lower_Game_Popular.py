from secrets import choice
from art_Popular import logo, vs
from Game_Data import data
import random

user_score = 0
computer_score = 0
is_Game_Over = False
continue_game = False
initial_record = {}
next_record = {}


def generate_random_record():
    return random.choice(data)


initial_record = generate_random_record()


def compare_scores():
    """ This function compares the follower counts of A and B and return the values accordingly"""

    if initial_record['follower_count'] > next_record['follower_count']:
        return 0
    elif initial_record['follower_count'] < next_record['follower_count']:
        return 1
    else:
        return 2


while not is_Game_Over:
    print(logo)
    next_record = generate_random_record()
    if continue_game:
        print(
            f"Congratulations!!!. You have guessed it Correct. Your Score is: {user_score}")
    else:
        print("***************** Let's Beging the Game ******************")
    print(
        f"Compare A: {initial_record['name']}, {initial_record['description']}, {initial_record['country']}")

    print(vs)
    print(
        f"Against B: {next_record['name']}, {next_record['description']}, {next_record['country']}")

    user_choice = input("Who has more followers?? Type A or B: ").lower()

    if user_choice in ['a', 'b']:
        result = compare_scores()

        if result == 2:
            print("Game is a DRAW...Guess Next time")
            continue_game = True
            initial_record = next_record

        if (user_choice == "a" and result == 0) or (user_choice == "b" and result == 1):
            user_score += 1
            continue_game = True
            initial_record = next_record
        else:
            computer_score += 1
            print(
                f"Opps....Computer WON the Game. Computer score is: {computer_score}")
            is_Game_Over = True
    else:
        print("Enter valid options (A/B)")
        is_Game_Over = True
