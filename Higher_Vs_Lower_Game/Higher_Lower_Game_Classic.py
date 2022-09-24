from random import randint

user_score = 0
computer_score = 0
is_Game_Over = False

MAX_GAME_TRIALS = 5
counter = 0


def random_number_generator():
    return randint(1, 100)


initial_random_number = random_number_generator()

while counter < MAX_GAME_TRIALS and not is_Game_Over:
    counter += 1
    next_random_number = random_number_generator()
    print(f"Your Openining Number is: {initial_random_number}")
    user_choice = input(
        "Choose your Guess is Less(L)/Greater(G) than Initial Number:").lower()
    if user_choice == "g" and next_random_number > initial_random_number:
        user_score += 1
        initial_random_number = next_random_number
    elif user_choice == "l" and next_random_number < initial_random_number:
        user_score += 1
        initial_random_number = next_random_number
    elif user_choice == "g" and next_random_number < initial_random_number:
        computer_score += 1
        is_Game_Over = True
    elif user_choice == "l" and next_random_number > initial_random_number:
        computer_score += 1
        is_Game_Over = True
    elif user_choice == "g" or user_choice == "l" and next_random_number == initial_random_number:
        print("Game is a Draw....")
    else:
        print("Enter valid Choice (G or L)")


if counter == MAX_GAME_TRIALS:
    print(
        f"You are the Real Winner and you have finished all the {MAX_GAME_TRIALS} levels !!!")
    print(f"You have played {counter} times and your score is: {user_score}")

if is_Game_Over:
    print(
        f"Well Played. Your total attempts is: {counter} and your score is: {user_score}")
