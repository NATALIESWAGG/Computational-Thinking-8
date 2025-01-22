# Beginning

import turtle

t = turtle.Turtle()

t.goto(100, 0)

#this is where I add color and the shape
colors = ["red","pink","orange"]
for i in range (5000000000000) :
    t.color (colors[ i % 3])
    t.forward (100 + i)
    t.left (146)

for i in range(50000000000000):
    t.forward( 100 + i)
    t.left(146)

# this is the ending 

turtle.exitonclick()