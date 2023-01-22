import turtle as tu

roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Pattern")
roo.left(90)
roo.speed(1000000000)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(20)

roo.right(90)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(20)

roo.left(270)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(20)

roo.right(90)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor('orange')
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(20)


def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(40)

roo.right(90)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(40)

roo.left(270)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(40)

roo.right(90)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor('orange')
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(40)


def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(60)

roo.right(90)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(60)

roo.left(270)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor("orange")
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(60)

roo.right(90)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(1)
        roo.pencolor('orange')
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(1)
        roo.backward(l)


draw(60)
wn.exitonclick()
