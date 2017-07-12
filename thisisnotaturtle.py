import turtle
t = turtle.Pen()
colors = ["red", "green", "blue", "purple", "orange"]
for x in range(300):
    t.forward(x)
    t.pencolor(colors[x%5])
    t.left(90)
    t.backward(200)
turtle.exitonclick()








