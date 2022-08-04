import turtle

def draw_sqaure(some_line):
    for i in range(1,5):
        some_line.forward(200)
        some_line.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(10)
    brad.pensize(2)
    for i in range(1,37):
        draw_sqaure(brad)
        brad.right(10)
    window.exitonclick()
draw_art()    