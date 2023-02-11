import random
import sys

moves = ["rock", "paper", "scissors"]

def computer_move(list):
  x = random.choice(moves)
  return x
  
def play(player, comp):
  print("Player: ", player, "   Computer: ", comp)
  if player == "rock":
    if comp == "rock":
      print("it's a draw!")
    elif comp == "scissors":
      print("You win!")
    else:
      print("You lost.")
  elif player == "paper":
    if comp == "rock":
      print("You win!")
    elif comp == "scissors":
      print("You lost.")
    else:
      print("It's a draw!")
  elif player == "scissors":
    if comp == "rock":
      print("You lost.")
    elif comp == "scissors":
      print("It's a draw!")
    else:
      print("You win!")
if len(sys.argv) > 1:
    # Retrieve the command line argument
    move = sys.argv[1]

    # Create a code name and print it to the screen
    play(move,computer_move(moves))
else:
    print('Error: You must provide the number of words as an argument.')
      
      