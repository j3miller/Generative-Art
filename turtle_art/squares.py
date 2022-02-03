# Imports
import turtle
import time
import random
import math
# from turtle_art.patterns import cool_test_pattern

# Turtle initialization
t = turtle.Turtle()
t.hideturtle()
turtle.screensize(1000, 1000)
turtle.colormode(255)
turtle.bgcolor('black')
turtle.mode("logo")     # Initial heading is north, pos angle is clockwise


def boundary_check(x_min, x_max, y_min, y_max):
    if x_min < -500:
        print("Hit the left boundary")
        return False
    if x_max > 500:
        print("Hit the right boundary")
        return False
    if y_min < -500:
        print("Hit the lower boundary")
        return False
    if y_max > 500:
        print("Hit the upper boundary")
        return False
    return True


def min_max_coordinates(x, y, size, angle):
    if (angle >= 0) and (angle < 90):
        angle_rads = math.radians(angle)
        a = size * math.sin(angle_rads)
        b = size * math.cos(angle_rads)
        x_min = x
        x_max = x + (a + b)
        y_max = y + b
        y_min = y - a
    if (angle >= 90) and (angle < 180):
        angle_rads = math.radians(angle - 90)
        a = size * math.sin(angle_rads)
        b = size * math.cos(angle_rads)
        x_min = x - b
        x_max = x + a
        y_min = y - (a + b)
        y_max = y
    if (angle >= 180) and (angle < 270):
        angle_rads = math.radians(angle - 180)
        a = size * math.sin(angle_rads)
        b = size * math.cos(angle_rads)
        x_min = x - (a + b)
        x_max = x
        y_min = y - b
        y_max = y + a
    if (angle >=270) and (angle < 360):
        angle_rads = math.radians(angle - 270)
        a = size * math.sin(angle_rads)
        b = size * math.cos(angle_rads)
        x_min = x - b
        x_max = x + a
        y_min = y
        y_max = y + a + b

    # print("""
    # x min: %s
    # x max: %s
    # y min: %s
    # y max: %s
    # """ % (x_min, x_max, y_min, y_max))
    return x_min, x_max, y_min, y_max
    # TODO: Change this to a touple


def draw_a_square_offset(x, y, size, angle):
    t.pu()
    t.showturtle()
    t.goto(x, y)
    t.setheading(angle)
    t.hideturtle()
    t.pd()
    for i in range(4):
        t.forward(size)
        t.right(90)


def simple_draw_a_square(x, y, size):
    t.pu()
    t.showturtle()
    t.goto(x, y)
    t.setheading(0)
    t.hideturtle()
    t.pd()
    for i in range(4):
        t.forward(size)
        t.right(90)


def draw_bound():
    t.pu()
    t.goto(-500, -500)
    t.setheading(0)
    t.pd()
    for i in range(4):
        t.forward(1000)
        t.right(90)


def generate_params(old_x, old_y, size, newseed):
    if newseed:
        random.seed(old_x + old_y)
    x = random.randrange(old_x, old_x + size, 1)
    y = random.randrange(old_y, old_y + size, 1)
    size = random.randrange(10, 100, 5)
    print("new params are: %s  %s  %s" % (x, y, size))
    return x, y, size


def main():
    # Turtle setup
    t.pencolor('white')
    t.pensize(3)
    t.speed(5)

    # Non-Turtle setup
    random.seed(73)
    total_squares = 100

    draw_bound()

    x, y, size = generate_params(-500, -500, 1000, False)
    simple_draw_a_square(x, y, size)
    for i in range(total_squares):
        x, y, size = generate_params(x, y, size, True)
        x_min, x_max, y_min, y_max = min_max_coordinates(x, y, size, 0)
        if boundary_check(x_min, x_max, y_min, y_max):
            draw_a_square_offset(x, y, size, 0)
        else:
            t.pencolor('cyan')
            draw_a_square_offset(x, y, size, 0)
            break


    # Turtle Cleanup
    turtle.done()


if __name__ == '__main__':
    main()
