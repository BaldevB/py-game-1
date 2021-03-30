
import random

player_score = computer_score = 0
valid_entries = ['0', '1']

while True:
  
  predict = random.randint(0,1)
 
  player_input = input("Enter either 1 or 0:")
  while player_input not in valid_entries:
    print("Invalid Input!")
    player_input = input("Please enter either 0 or 1: ")
   
  player_input = int(player_input)
 
  if predict == player_input:
    computer_score = computer_score + 1
    print("Computer score ",computer_score)
    print("Player score ",player_score)
  else:
    player_score = player_score + 1
    print("Computer score ",computer_score)
    print("Player score ",player_score)

  if computer_score == 10:
    print("Bad Luck, Computer Wins!")
    break
  elif player_score == 10:
    print("Congrats, You Won!")
    break