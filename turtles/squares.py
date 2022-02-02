# Imports
import turtle
import time
import random

# Turtle initialization
t = turtle.Turtle()
t.hideturtle()
turtle.screensize(1000, 1000)
turtle.colormode(255)
turtle.bgcolor('black')
turtle.mode("logo")     # Initial heading is north, pos angle is clockwise


def simple_check_in_bounds(x, y, size):
    if x + size > 500:
        return False
    if y + size > 500:
        return False
    if x < -500:
        return False
    if y < -500:
        return False
    return True


def simple_draw_a_square(x, y, size):
    t.pu()
    t.showturtle()
    t.goto(x, y)
    t.setheading(0)
    t.pd()
    for i in range(4):
        t.forward(size)
        t.right(90)


def generate_initial_params():
    x = random.randrange(-500, 500, 1)
    y = random.randrange(-500, 500, 1)
    size = random.randrange(10, 100, 5)
    print("initial params are: %s  %s  %s" % (x, y, size))
    return x, y, size


def main():
    # Turtle setup
    t.pencolor('white')
    t.pensize(3)

    # Non-Turtle setup
    random.seed(73)
    total_squares = 10

    for i in range(total_squares):
        x, y, size = generate_initial_params()
        simple_draw_a_square(x, y, size)
    # Turtle Cleanup
    turtle.done()


if __name__ == '__main__':
    main()
