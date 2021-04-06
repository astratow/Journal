#import colorgram
import turtle as turtle_mod
import random
from rainbow import rgb_colors

turtle_mod.colormode(255)
tim = turtle_mod.Turtle()
tim.setpos(-250, 250)
#rgb_colors = [(141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181), (118, 117, 163), (3, 111, 115), (87, 51, 49), (62, 59, 77), (35, 37, 36)]
# colors = colorgram.extract('img/image.jpeg', 100)
#
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

#print(rgb_colors)


for _ in range(10):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
tim.setheading(270)
tim.forward(50)
tim.setheading(180)
tim.forward(500)

screen = turtle_mod.Screen()
screen.exitonclick()