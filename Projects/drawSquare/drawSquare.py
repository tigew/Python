import turtle


def spawnWindow():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(100)

    for i in range(1, 100):
        drawTriangle(brad)
        brad.right(10)

    # Draw stem
    brad.penup()
    brad.setpos(85, -25)
    brad.pendown()
    brad.setheading(270)
    brad.color("blue")
    brad.forward(300)

    window.exitonclick()

    # Square
''' for i in range(1, 37):
        drawSquare(brad)
        brad.right(10) '''

# drawCircle()


def drawSquare(myTurtle):

    for i in range(1, 5):
        myTurtle.forward(100)
        myTurtle.right(90)


def drawCircle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def drawTriangle(myTurtle):

    for i in range(1, 4):
        myTurtle.forward(200)
        myTurtle.right(135)


spawnWindow()
