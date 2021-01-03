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
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
#    elif wall_on_right():
#        if wall_in_front():
#            turn_left()
#            move()
    else:
        turn_left()
        
        

