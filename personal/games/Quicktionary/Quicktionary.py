import random as rand
import turtle as trtl

'''Setup'''

# Variables
players = {} # Player Stats
topics = [] # Yellow Cards
wdlength = [] # Blue Cards
let_req = [] # Red Cards
current_red = ""
current_blue = ""
current_yellow = ""
round_number = 1
font_setup = ("Arial", 20, "normal")
turtles = []
x = -375
y = 200

# Create the players
num_player = int(input("How many players? "))
for player in range(num_player):
  name = input("What is player {}'s name? ".format(player+1))
  players[player] = {'name' : name, 'score' : 0}

# Analyze the Yellow Card contents and produce the deck
yellow_card = open("yellow.txt", "r")
for line in yellow_card:
  topic = ""
  index = 0
  while (line[index] != "\n"):
    topic = topic + line[index]
    index += 1
  topics.append(topic)
yellow_card.close()

# Analyze the Blue Card contents and produce the deck
blue_card = open("blue.txt", "r")
for line in blue_card:
  length = ""
  index = 0
  while (line[index] != "\n"):
    length = length + line[index]
    index += 1
  wdlength.append(length)
blue_card.close()

# Analyze the Red Card contents and produce the deck
red_card = open("red.txt", "r")
for line in red_card:
  letters = ""
  index = 0
  while (line[index] != "\n"):
    letters = letters + line[index]
    index += 1
  let_req.append(letters)
red_card.close()

# Make scoreboard
#screen
wn = trtl.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("black")
#Static word display
wn.tracer(False)
title = trtl.Turtle()
title.pencolor("lime")
title.penup()
title.hideturtle()
title.goto(-110,225)
title.write("SCOREBOARD", font=font_setup)
title.goto(-70,-225)
title.write("Round", font=font_setup)

#round number tracker
rndnum = trtl.Turtle()
rndnum.pencolor("lime")
rndnum.penup()
rndnum.hideturtle()
rndnum.goto(25,-225)
rndnum.write(round_number, font=font_setup)

#Finish line
finish = trtl.Turtle()
finish.hideturtle()
finish.pencolor("white")
finish.pensize(4)
finish.penup()
finish.goto(300,225)
finish.setheading(270)
finish.write(" Finish!", font=font_setup)
finish.pendown()
finish.forward(400)

#player trackers
for i in range(num_player):
  turtles.append(trtl.Turtle())
  turtles[i].color("white")
  turtles[i].pensize(2)
  turtles[i].penup()
  turtles[i].goto(x,y)
  turtles[i].pendown()
  turtles[i].write(players[i]['name'])
  y = y - (400/num_player)
wn.tracer(True)


'''Functions'''

# Update the player score value
def update_score(card_swap, winner):
  global players
  if card_swap[0] == "y":
    players[winner]['score'] += 1
    turtles[winner].pencolor("yellow")
    turtles[winner].forward(150)
  elif card_swap[0] == "b":
    players[winner]['score'] += 1
    turtles[winner].pencolor("blue")
    turtles[winner].forward(150)
  elif card_swap[0] == "r":
    players[winner]['score'] += 1
    turtles[winner].pencolor("red")
    turtles[winner].forward(150)

# Display the player scores to the console
def display_score():
  global round_number
  for player in players.values():
    print(player.get('name'), player.get('score'))
    check = player.get('score')
    if check == 5:
      print("\nWinner!", player.get('name') + "\n")
      round_number = None
      return False

# select new cards
def select_red():
  global current_red
  current_red = rand.choice(let_req)
  print("Red: " + current_red)
  let_req.remove(current_red)

def select_blue():
  global current_blue
  current_blue = rand.choice(wdlength)
  print("Blue: " + current_blue)
  wdlength.remove(current_blue)

def select_yellow():
  global current_yellow
  current_yellow = rand.choice(topics)
  print("\nYellow: " + current_yellow)
  topics.remove(current_yellow)

def clearBoard():
  global y
  y = 200
  wn.tracer(False)
  for i in range(num_player):
    turtles[i].clear()
    turtles[i].pencolor("white")
    turtles[i].penup()
    turtles[i].goto(x,y)
    turtles[i].write(players[i]['name'])
    turtles[i].pendown()
    y = y - (400/num_player)
  wn.tracer(True)

# if wanted, repeat game
def repeat():
  global round_number
  repeat = input("Would you like to play again? ").lower()
  if repeat[0] == "y":
    print("\n\n")
    round_number = 0
    for player in players.values():
      player['score'] = 0
    rndnum.clear()
    rndnum.write(round_number, font=font_setup)
    clearBoard()
    main()
    
# Cycle the round and change the scoreboard display
def newRound():
  global round_number
  round_number += 1
  rndnum.clear()
  rndnum.write(round_number, font=font_setup)

# Main Game code
def main():

  select_yellow()
  select_blue()
  select_red()

  while True:
    print("ROUND NUMBER:", round_number)

    winner = int(input("Which player won? (player number) ")) - 1
    card_swap = input("What card would you like to take? (yellow/blue/red) ").lower()

    update_score(card_swap, winner)

    if card_swap[0] == "y":
      select_yellow()
      print("Blue: " + current_blue)
      print("Red: " + current_red)

    elif card_swap[0] == "b":
      print("\nYellow: " + current_yellow)
      select_blue()
      print("Red: " + current_red)

    elif card_swap[0] == "r":
      print("\nYellow: " + current_yellow)
      print("Blue: " + current_blue)
      select_red()

    elif card_swap == "quit":
      break

    else:
      print("\nYellow: " + current_yellow)
      print("Blue: " + current_blue)
      print("Red: " + current_red)

    if display_score() == False:
      break

    newRound()

  repeat()


'''Initialize!'''

print("\nWelcome to Quicktionary!\n")
main()
