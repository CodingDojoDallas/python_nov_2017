import turtle
# simple snowman
radius = -10
for x in range(1,5):
    turtle.circle(radius)
    turtle.circle(radius, 180)
    radius*=-2
