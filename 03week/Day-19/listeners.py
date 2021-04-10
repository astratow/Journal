from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
	'''Moves Turtle Forward'''
	tim.forward(10)
	
screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
