from menu import MENU
from menu import resources

total_amount = 0
is_switch_on = True


def is_enough_resources(ingredients):
    """ This function checks whether the sufficient resources to process the order"""
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """ This function returns the sums the coins entered by the user"""
    print("Please insert coins")
    amount = int(input("How many Quarters?:")) * 0.25
    amount += int(input("How many Dimes?:")) * 0.1
    amount += int(input("How many Nickels?:")) * 0.05
    amount += int(input("How many Pennies?:")) * 0.01
    return amount


def is_valid_order(amount, drink_cost):
    """ This function returns the change after processing the order"""
    if amount > drink_cost:
        change = round(amount - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global total_amount
        total_amount += drink_cost
        return True
    elif amount == drink_cost:
        print("You have given exact change...")
        return True
    else:
        return False


def process_order(choice, ingredients):
    """ This function process the order and print the result"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice}. Enjoy!!!")


def print_report():
    """ This function prints the report of resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_amount}")


while is_switch_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if is_enough_resources(MENU[user_choice]['ingredients']):
            user_amount = process_coins()
            if is_valid_order(user_amount, MENU[user_choice]['cost']):
                process_order(user_choice,MENU[user_choice]['ingredients'])
    elif user_choice == "off":
        switch_off = False
    elif user_choice == "report":
        print_report()
    else:
        print("Invalid Choice selected. Please select correct choice...")