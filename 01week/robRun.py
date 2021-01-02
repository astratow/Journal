#RobotRun! is a program to run along hurdle challenge on https://reeborg.ca/reeborg.html website
def turn_right():
    for step in range(3):
        turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()