import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

"""This function will do following 
1. calculate total score for a given list
2. return 0 if the list has Black Jack (Q (10) or K(10) or Jocker (10) with ACE (11)
3. replace 11 with 1 if list sum has more than 21 """


def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0

    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


"""This function compares the user and computer scores and return the results accordingly
 """


def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Draw..."
    elif computer_score == 0:
        return "User Lose...Computer has a Black Jack"
    elif user_score == 0:
        return "Computer Lose, User has a Black Jack"
    elif user_score > 21:
        return "User Went Over...Computer Wins!!!"
    elif computer_score > 21:
        return "Computer Went Over...User Wins!!!"
    elif user_score > computer_score:
        return "User Wins!!!"
    else:
        return "User Lose..."


def deal_card():
    return random.choice(cards)


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_Game_Over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_Game_Over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User Cards: {user_cards} and User_Score is: {user_score}")
        print(f"Computer First Card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_Game_Over = True
        else:
            user_choice = input(
                "Type 'y' to get another card, Type 'n' to pass:")
            if user_choice.casefold() == 'y':
                user_cards.append(deal_card())
            else:
                is_Game_Over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"User final hand is: {user_cards}, final score is: {user_score}")
    print(
        f"Computer final hand is: {computer_cards}, final score is: {computer_score}")
    print(compare_scores(user_score, computer_score))


while (input("Do you want to play Black Jack Game?? (y/n)").casefold() == 'y'):
    play_game()
