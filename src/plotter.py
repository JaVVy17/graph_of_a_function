from turtle import *
from function import *
SCALE = 20


def grid():
    border = 20
    right(90)
    for x in range(-border, border + 1):
        up()
        goto(x * SCALE, border * SCALE)
        down()
        fd(40 * SCALE)
        width(0)
        if x == -1:
            width(4)

    left(90)
    for y in range(-border, border + 1 ):
        up()
        goto(-border * SCALE, y * SCALE, )
        down()
        fd(40 * SCALE)
        width(0)
        if y == -1:
            width(4)

def draw_function(funct, x_range, func_color, *args):
    grid()
    color(func_color), width(3), up()
    x = -20
    while x < x_range:
        y = funct(x, *args)
        goto(x * 20, y * 20)
        down()
        x += 0.1

def zeroing():
    color('black')
    width(0)
    print("-------------")

def main():
    speed(0), tracer(3), title("Графики функций")

    draw_function(linear, 20, "blue", int(input('Введите k:')), int(input('Введите b:')))
    zeroing()

    draw_function(parabola, 20, "green", int(input('Введите a:')), int(input('Введите b:')), int(input('Введите c:')))
    zeroing()

    mainloop()


if __name__ == "__main__":
    main()