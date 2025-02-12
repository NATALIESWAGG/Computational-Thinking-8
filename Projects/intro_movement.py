# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass ()

stage.set_background("moon")
s1 = codesters.Sprite ("person1",0,-200)
s1.set_size (0.5)



# Section 2: define controls
def move_up (sprite):
    sprite.move_up(1)

    def move_down (sprite):
        sprite.move_left(1)

def move_left(sprite):
    