import turtle
t = turtle.Turtle()


def main():
    t.hideturtle()
    for i in range(4):
        t.forward(100)
        t.right(90)
    turtle.done()


if __name__ == '__main__':
    main()
