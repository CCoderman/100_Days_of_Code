# Reeborg's World Challenge "Lost in a Maze"
# https://reeborg.ca/reeborg.html?
# lang=en&mode=python&menu=worlds%2
# Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def find_goal():
    while not at_goal():
        if wall_on_right():
            if wall_in_front():
                turn_left()
            elif front_is_clear():
                move()
        else:
            turn_right()
            move()


find_goal()