import turtle
t = turtle.Turtle()
turtle.bgcolor('black')


def color_test():
    r = 100
    g = 100
    b = 10
    t.pencolor((r, g, b))
    t.forward(100)
    t.pencolor((100, 100, 10))
    t.right(90)
    t.forward(100)


def gradient_test():
    # Set up color variables
    r = 100
    g = 100
    b = 100

    # Move turtle to initial position
    t.speed(5)
    t.penup()
    t.goto(-100, -255)
    t.pendown()
    t.right(180)
    t.width(3)
    r = 0
    for i in range(255):
        r = i
        r = r % 255
        t.pencolor(r, g, b)
        t.forward(2)


def fill_test():
    t.pu()
    t.goto(-300, 100)
    t.pencolor('white')
    t.fillcolor(150, 200, 12)
    t.begin_fill()
    t.pd()
    for i in range(4):
        t.forward(200)
        t.right(90)
    t.end_fill()

    t.pu()
    t.goto(-100, 100)
    t.fillcolor(200, 12, 200)
    t.begin_fill()
    t.pd()
    for i in range(4):
        t.forward(200)
        t.right(90)
    t.end_fill()


def palette_test():
    return


def main():
    # Turtle Setup
    t.hideturtle()
    turtle.colormode(255)

    # Function Call
    # color_test()
    # gradient_test()
    fill_test()

    # Turtle Cleanup
    turtle.done()


if __name__ == '__main__':
    main()
