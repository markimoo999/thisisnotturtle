import turtle
t = turtle.Pen()

colors = ["red", "green", "blue", "yellow", "pink"]
turtle.bgcolor("black")
def polygon(sides, degree, length):
    for x in range(0, sides):
        t.pencolor(colors[x%5])
        t.forward(length)
        t.right(degree)
while True == True:
    shape = raw_input("enter a shape that i can make with turtle. if you say no, you can X out of the program.\n")
    if shape == "square" or shape == "Square":
        polygon(4, 90, 90)
        t.clear()
    elif shape == "triangle" or shape == "Triangle":
        polygon(3, 120, 100)
        t.clear()
    elif shape == "pentagon" or shape == "Pentagon":
        polygon(5, 72, 100)
        t.clear()
    elif shape == "circle" or shape == "Circle":
        t.penup()
        t.goto(0, 100)
        t.pendown()
        polygon(22, 360/21, 50)
        t.clear()
    elif shape == "no" or shape == "No":
        break
    else:
        print"go back to school. that's not a shape."
turtle.exitonclick()