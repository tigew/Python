import turtle


def spawnWindow():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(1)

    drawSquare(brad)
    drawCircle()

    window.exitonclick()


def drawSquare(myTurtle):

    for i in range(1, 5):
        myTurtle.forward(100)
        myTurtle.right(90)


def drawCircle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


''' def drawTriangle():
    trike = turtle.Turtle()
    trike.shape("turtle")
    trike.color("purple")
    
    trike.right(45)
    trike.forward(100)
    trike.right(135)
    trike.forward(100)
    trike.right(135)
    trike.forward(100) '''

spawnWindow()
