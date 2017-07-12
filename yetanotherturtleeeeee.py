import turtle
import time
t = turtle.Pen()
colors = ["red", "green", "blue", "yellow", "pink", "purple", "white", "orange"]
turtle.bgcolor("black")
def polygon(sides, degree, length):
    for x in range(0, sides):
        t.pencolor(colors[x%8])
        t.forward(length)
        t.right(degree)
while True == True:
    t.penup()
    t.goto(0, 100)
    t.pendown()
    shape = raw_input("enter a shape that i can make with turtle. if you say no, you can X out of the program.\n")
    if shape== "no" or shape == "No":
        break
    else:
        diction = {"triangle": [3, 120, 100], "square": [4, 90, 90],"pentagon": [5, 72, 100], "circle": [100, 50, 8], "hexagon": [6, 60, 100], "heptagon": [7, 51.5, 100], "octagon": [8, 45, 100], "enneagon": [9, 39.99, 100], "decagon": [10, 36, 90]}
        ar = diction[shape]
        polygon(ar[0], ar[1], ar[2])
        time.sleep(2)
        t.clear()


