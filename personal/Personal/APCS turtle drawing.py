'''#Import turtle module
import turtle as trtl

#create turtle widget
painter = trtl.Turtle()
painter.pensize(1)

#Outer square
painter.penup()
painter.goto(-141.42135,0)
painter.pendown()

c = input("What color would you like the outer square?")
painter.fillcolor(c)
painter.begin_fill()
painter.right(45)
painter.forward(200)
painter.left(90)
painter.forward(200)
painter.left(90)
painter.forward(200)
painter.left(90)
painter.forward(200)
painter.end_fill()

#inner square
painter.penup()
painter.goto(-70.71068,-70.71068)
painter.pendown()

x = input("What color would you like the inner square to be?")
painter.fillcolor(x)
painter.begin_fill()
painter.left(135)
painter.forward(141.42135)
painter.left(90)
painter.forward(141.42135)
painter.left(90)
painter.forward(141.42135)
painter.left(90)
painter.forward(141.42135)
painter.end_fill()

#inner circle

painter.penup()
painter.goto(-70.71068,0)
painter.pendown()

z = input("What color would you like the circle to be?")
painter.fillcolor(z)
painter.begin_fill()
painter.circle(70.71068)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()


import turtle
import random
turtle.colormode(255)

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
r = random.randint(100, 255)
g = random.randint(100, 255)
b = random.randint(100, 255)
for n in range(50):
    t.pencolor((r, g, b))
    size = random.randint(10, 40)
    sides = random.randint(3, 8)
    thick = random.randint(1, 6)
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(360/sides + 1)
        angle = t.heading()
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    t.setheading(angle - 90)
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(360/sides + 1)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    t.setheading(angle - 180)
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(360/sides + 1)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    t.setheading(angle - 270)
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(360/sides + 1)
'''
'''

import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("orange")
turtle_list.append(temp_turtle)

turtle_list[0].forward(500)
turtle_list[1].setheading(45)
turtle_list[1].forward(500)
turtle_list[2].setheading(315)
turtle_list[2].forward(500)
turtle_list[3].setheading(180)
turtle_list[3].forward(500)

print(turtle_list)

trtl.mainloop()
'''
'''
players = []

num_player = int(input("How many players? "))
for player in range(num_player):
  players.append(list())

print(players)

score = input()
players[1].append(score)
print(players)
'''