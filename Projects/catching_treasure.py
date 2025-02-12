# Section 1 - setup

import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()

player = codesters.Sprite("gem")
stage.set_background("Gem mine")
# starting speed
object_speed = 2

#starting value
collected_treasure = 0

# Section 2 - objects
def falling_objects():
    global object_speed,collected_treasure
    if treasure_collected <32:
        # the game is not over
    
    x = randem.randint(-250,250)
    y = 250

    object = codesters.Sprite("gems", x, y)
    object.set_size (1)

# # control keys
#  player.event_key("a",left)
# ("d",right)


