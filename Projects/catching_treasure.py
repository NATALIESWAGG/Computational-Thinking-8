# Section 1 - setup

import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_all_walls()

player = codesters.Sprite("tin")
player.set_size(.15)
stage.set_background("Gem mine")
# starting speed
object_speed = -2

#starting value
collected_treasure = 0

# Section 2 - objects
def falling_objects():
    global object_speed,collected_treasure
    if collected_treasure <32:
        # the game is not over
    
        x = random.randint(-250,250)
        y = 250

        object = codesters.Sprite("gem", x, y)
        object.set_size (.10)
        object.set_y_speed(object_speed)

    # the blank below is a number in seconds
    #   between each object
stage.event_interval (falling_objects, 4)


# Section 3 - collision
def collision(player, object):
    global collected_treasure
    if object.get_image_name() == "gem":
        stage.remove_sprite(object)
        collected_treasure+=1
        if collected_treasure>=32:
            player.say (f"You collected all the treasure - you win!",5)
        else:
            player.say (f"{collected_treasure} treasure_collected", 0.5)
player.event_collision(collision)

# Section 4 - movement

#control keys (fill in both blanks)

# a key
def go_left():
    player.move_left(10)

# d key
def go_right():
    player.move_right(10)
    

player.event_key("a", go_left)
player.event_key("d", go_right)




