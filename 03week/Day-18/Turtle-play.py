import turtle as t
import random
tim = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
#colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 100, 270]
tim.pensize(20)
tim.speed('fastest')

for _ in range(200):
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(random.choice(directions))

screen = Screen()

screen.exitonclick()