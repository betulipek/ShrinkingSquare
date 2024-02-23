import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light yellow")
turtle_screen.title("Shrinking Square")

shrinking = turtle.Turtle()
shrinking.color("brown")


def square(size):
    for squarex in range(4):
        shrinking.forward(size)
        shrinking.left(90)
        size = size -5


square(150)
square(130)
square(110)
square(90)
square(70)
square(50)
square(30)
square(10)
square(-10)



turtle.done()

