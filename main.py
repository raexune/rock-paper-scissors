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

import random

player1 = random.randint(1, 3)


print("Player 1: ")
if player1 == 1:
  print(rock)
elif player1 == 2:
  print(paper)
elif player1 == 3:
  print(scissors)

player2 = random.randint(0, 2)

print("Player 2: ")
if player2 == 1:
  print(rock)
elif player2 == 2:
  print(paper)
elif player2 == 3:
  print(scissors)

if player1 == 1 and player2 == 3:
  print("Player 1 wins.")
elif player1 == 3 and player2 == 1:
  print("Player 2 wins")
elif player1 == 2 and player2 == 1:
  print("Player 1 wins.")
elif player1 == 1 and player2 == 2:
  print("Player 2 wins.")
elif player1 == 3 and player2 == 2:
  print("Player1 wins.")
elif player1 == 2 and player2 == 3:
  print("Player 2 wins.")
else:
  print("It´s a draw.")

