# Imports
import turtle
import time
import random
import math

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


def rotational_check_in_bounds(x, y, size, angle):
    if angle == 0:  # Bottom left start
        if x < -500 or y < -500:
            return False
        if x + size > 500 or y + size > 500:
            return False
        return True
    if angle == 90: # Top left start
        if x < -500 or y > 500:
            return False
        if x + size > 500 or y - size < -500:
            return False
        return True
    if angle == 180: # Top right start
        if x > 500 or y > 500:
            return False
        if x - size < -500 or y - size < -500:
            return False
        return True
    if angle == 270: # Bottom right start
        if x > 500 or y < -500:
            return False
        if x - size < -500 or y + size > 500:
            return False
        return True
    else:
        print("Non-right angle, I'm not brave enough")
        return False


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

    print("""
    x min: %s
    x max: %s
    y min: %s
    y max: %s
    """ % (x_min, x_max, y_min, y_max))


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
    t.setheading(90)
    t.hideturtle()
    t.pd()
    for i in range(4):
        t.forward(size)
        t.right(90)


def generate_params(old_x, old_y, size, newseed):
    if newseed:
        random.seed(old_x + old_y)
    x = random.randrange(old_x, old_x + size, 1)
    y = random.randrange(old_y, old_y + size, 1)
    size = random.randrange(10, 100, 5)
    print("new params are: %s  %s  %s" % (x, y, size))
    return x, y, size


def angular_offset_test_simple():
    t.pencolor('white')
    draw_a_square_offset(0, 0, 100, 0)
    print(rotational_check_in_bounds(0, 0, 100, 0))
    t.pencolor('red')
    draw_a_square_offset(0, 0, 100, 90)
    print(rotational_check_in_bounds(0, 0, 100, 90))
    t.pencolor('green')
    draw_a_square_offset(0, 0, 100, 180)
    print(rotational_check_in_bounds(0, 0, 100, 180))
    t.pencolor('blue')
    draw_a_square_offset(0, 0, 100, 270)
    print(rotational_check_in_bounds(0, 0, 100, 270))


def angular_offset_test_modular(color, x, y, size, angle):
    t.pencolor(color)
    draw_a_square_offset(x, y, size, angle)
    print(rotational_check_in_bounds(x, y, size, angle))


def angular_offset_test():
    angular_offset_test_modular('white', 0, 0, 100, 0)
    angular_offset_test_modular('white', 250, 0, 100, 0)
    angular_offset_test_modular('white', 500, 0, 100, 0)


def main():
    # Turtle setup
    t.pencolor('white')
    t.pensize(3)
    t.speed(5)

    # Non-Turtle setup
    random.seed(73)
    total_squares = 1

    # angular_offset_test()
    draw_a_square_offset(0, 0, 100, 0)
    min_max_coordinates(0, 0, 100, 0)
    draw_a_square_offset(0, 0, 100, 45)
    min_max_coordinates(0, 0, 100, 45)

    draw_a_square_offset(0, 0, 100, 90)
    min_max_coordinates(0, 0, 100, 90)
    draw_a_square_offset(0, 0, 100, 135)
    min_max_coordinates(0, 0, 100, 135)

    draw_a_square_offset(0, 0, 100, 180)
    min_max_coordinates(0, 0, 100, 180)
    draw_a_square_offset(0, 0, 100, 225)
    min_max_coordinates(0, 0, 100, 225)

    draw_a_square_offset(0, 0, 100, 270)
    min_max_coordinates(0, 0, 100, 270)
    draw_a_square_offset(0, 0, 100, 315)
    min_max_coordinates(0, 0, 100, 315)

    # x, y, size = generate_params(-500, -500, 1000, False)
    # simple_draw_a_square(x, y, size)

    for i in range(total_squares - 1):
        x, y, size = generate_params(x, y, size, True)
        if simple_check_in_bounds(x, y, size):
            simple_draw_a_square(x, y, size)
        else:
            print("Out of bounds: %s  %s  %s " % (x, y, size))
            break

    # Turtle Cleanup
    turtle.done()


if __name__ == '__main__':
    main()
