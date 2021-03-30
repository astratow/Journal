import turtle as t

tim = t.Turtle()
screen = t.Screen()

for _ in range(0, 15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
	
screen.exitonclick()