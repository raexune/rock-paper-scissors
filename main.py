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

while True:
  
  player1 = int(input("Choose 0 for rock, 1 for Paper or 2 for Scissors: "))

  if player1 <0 or player1 >=3:
    print("Wrong input.")
  else:
    print("Player 1: ")
    if player1 == 0:
      print(rock)
    elif player1 == 1:
      print(paper)
    elif player1 == 2:
      print(scissors)

  player2 = random.randint(0, 2)

  print("Player 2: ")
  if player2 == 0:
    print(rock)
  elif player2 == 1:
    print(paper)
  elif player2 == 2:
    print(scissors)

  if player1 == 0 and player2 == 2:
    print("Player 1 wins.")
  elif player1 == 2 and player2 == 0:
    print("Player 2 wins")
  elif player1 == 1 and player2 == 0:
    print("Player 1 wins.")
  elif player1 == 0 and player2 == 1:
    print("Player 2 wins.")
  elif player1 == 2 and player2 == 1:
    print("Player1 wins.")
  elif player1 == 1 and player2 == 2:
    print("Player 2 wins.")
  else:
    print("It´s a draw.")


