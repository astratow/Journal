import turtle as t

#objects
tim = t.Turtle()
screen = t.Screen()

#variable that contains number of sides, 3 for triangle as minumum 

number_of_sides = 3

while number_of_sides < 10:
    #mathematical scheme to get an angle of the shape
    angle = 360 / number_of_sides
    #for loop takes number of sides and it repeats until it reaches shape
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)
    #adds side to the shape
    number_of_sides = number_of_sides + 1
    


screen.exitonclick()
