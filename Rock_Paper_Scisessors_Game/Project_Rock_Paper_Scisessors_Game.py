### ************************Rock Paper Scissors Game ********************************

import random

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

#Write your code below this line 👇

print("************************Rock Paper Scissors Game ********************************")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print("You have choosen")
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)  
else:
  print("Invalid Selection")
  exit(0)

rand_int = random.randint(0,2)
print(rand_int)

print("Computer have choosen")
if rand_int == 0:
  print(rock)
elif rand_int == 1:
  print(paper)
else:
  print(scissors)  

if choice == 0 and rand_int == 2:
  print("You Win")
elif choice == 2 and rand_int == 1:
  print("You Win")
elif choice == 1 and rand_int == 0:
  print("You Win")
elif choice == rand_int:
  print("Game Draw!!!")  
else:
  print("You lose")