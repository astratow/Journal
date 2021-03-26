from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

i = 0
while i < 4:
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(200)
    i += 1
    

screen = Screen()

screen.exitonclick()