#MazePathFinder this app is looking for a path to the goal in random maze at https://reeborg.ca/reeborg.html
def turn_right():
    for step in range(3):
        turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()