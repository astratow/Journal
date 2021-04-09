#import colorgram
import turtle as turtle_mod
import random
from rainbow import rgb_colors

turtle_mod.colormode(255)
tim = turtle_mod.Turtle()
tim.speed('fastest')
tim.ht() #hides tim
tim.penup() #hides lines
tim.setpos(-250, 250) #sets position
tim.setheading(0) #sets direction
tim.forward(10)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(270)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_mod.Screen()
screen.exitonclick()