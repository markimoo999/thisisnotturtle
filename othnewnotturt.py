import turtle
t = turtle.Pen()
colors = ["red", "green", "blue", "yellow"]
turtle.bgcolor("black")
def polygon(sides, degree, length):
    for x in range(0, sides):
        t.pencolor(colors[x%4])
        t.forward(length)
        t.right(degree)
polygon(4, 90, 90)
t.clear()
polygon(3, 120, 100)
turtle.exitonclick()