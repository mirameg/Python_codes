import turtle
turtle.speed(0)

def rectangle():
    for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

def star(size):
    for s in range(5):
        turtle.forward(size)
        turtle.left(144)

turtle.color("dark red")
turtle.begin_fill()
rectangle()
turtle.end_fill()

# Big star
turtle.penup()
turtle.goto(0,50)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
star(40)
turtle.end_fill()

# small star 1
turtle.penup()
turtle.goto(50,70)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
star(10)
turtle.end_fill()


# small star 2
turtle.penup()
turtle.goto(67,55)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
star(10)
turtle.end_fill()

# small star 3
turtle.penup()
turtle.goto(60,40)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
star(10)
turtle.end_fill()

# small star 3
turtle.penup()
turtle.goto(45,30)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
star(10)
turtle.end_fill()


turtle.penup()
turtle.goto(150,0)
turtle.pendown()
style = ("Courier", 10, "bold")
turtle.write("China Flag", font = style, align = "center")


turtle.penup()
turtle.goto(150,-10)
turtle.pendown()
style = ("Courier", 10, "italic")
turtle.write("By Meg", font = style, align = "center")

turtle.ht()
