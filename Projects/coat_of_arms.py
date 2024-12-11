###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("spring")
q1 = codesters.Triangle(100,100,200, 'orange')
q2 = codesters.Triangle(-100,100,200, 'purple')
q3 = codesters.Triangle(-100,-100,200, 'red')
q4 = codesters.Triangle(100,-100,200, 'pink')


s1 = codesters.Sprite ("cardinal", 100, 100)
s1.set_size(0.7)
s2 = codesters.Sprite ("images (2)", -100, -100)
s2.set_size(1.1)
s3 = codesters.Sprite ("download.png", 100, -100)
s3.set_size(0.9)
s4 = codesters.Sprite ("cat", -100, 100)
s4.set_size(0.3)


message1 = codesters.Text ("Natalie Hartman",0,220,"purple")
message2 = codesters.Text ("carpe diem",0,-220,"black")