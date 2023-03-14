#Day 4 - Randomisation and Python Lists

#Concepts Practised: randomisation and python lists

#Rock Paper Scissors:
import random
import sys

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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors 0/1/2:"))

if user == 0:
	print("You chose: Rock")
	print(rock)
elif user == 1:
	print("You chose: Paper")
	print(paper)
elif user == 2:
	print("You chose: Scissors")
	print(scissors)
else:
	print("ERROR! Enter a number 0/1/2")
	sys.exit()

computer = random.randint(0,2)
if computer == 0:
	print("The computer chose: Rock")
	print(rock)
elif computer == 1:
	print("The computer chose: Paper")
	print(paper)
elif computer == 2:
	print("The computer chose: Scissors")
	print(scissors)

if computer == user:
	print("it s a draw")
elif user == 0 and computer == 1:
	print("You lost")
elif user == 1 and computer == 2:
	print("You lost")
elif user == 2 and computer == 0:
	print("You lost")
elif user == 0 and computer == 2:
	print("You Win")
elif user == 1 and computer == 0:
	print("You Win")
elif user == 2 and computer == 1:
	print("You Win")