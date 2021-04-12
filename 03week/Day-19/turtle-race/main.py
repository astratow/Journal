from turtle import Turtle, Screen
import random 
import easy_gui as eg

race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make a bet', prompt='Which turtle will win the race? Enter a colour: ')
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []

#create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle
        if turtle.xcor() > 230:
            race_on= False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
        #make turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        
        
screen.exitonclick()

# tim_red = Turtle()
# tim_red = Turtle(shape="turtle")
# tim_red.color('red')
# tim_red.penup()
# tim_red.goto(x=-230, y=-120)

# tim_green = Turtle()
# tim_green = Turtle(shape="turtle")
# tim_green.color('green')
# tim_green.penup()
# tim_green.goto(x=-230, y=-80)

# tim_orange = Turtle()
# tim_orange = Turtle(shape="turtle")
# tim_orange.color('orange')
# tim_orange.penup()
# tim_orange.goto(x=-230, y=-40)

# tim_purple = Turtle()
# tim_purple = Turtle(shape="turtle")
# tim_purple.color('purple')
# tim_purple.penup()
# tim_purple.goto(x=-230, y=0)

# tim_yellow = Turtle()
# tim_yellow = Turtle(shape="turtle")
# tim_yellow.color('yellow')
# tim_yellow.penup()
# tim_yellow.goto(x=-230, y=40)

# tim_blue = Turtle()
# tim_blue = Turtle(shape="turtle")
# tim_blue.color('blue')
# tim_blue.penup()
# tim_blue.goto(x=-230, y=80)