#Optional Python Turtle

import turtle
# the distance we want the pointer to travel each time
DIST = 4
turtle.color("red", "green")
for x in range(100):
    print "x", x
    for y in range(1,50):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(DIST)
        # advance according to set distance
        #turtle.forward(DIST)

        turtle.left(10)


        turtle.forward(DIST)
    # add to set distance
    DIST += 1


turtle.done()

