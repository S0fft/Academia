import turtle

window = turtle.Screen()
window.title("computer_graphics_2 - DSEA")

turtle.speed(0)
turtle.pensize(2)
turtle.left(90)
turtle.backward(100)
turtle.color("green")


def draw_tree(l):
    if l < 10:
        return
    else:
        turtle.forward(l)
        turtle.color("red")
        turtle.circle(2)
        turtle.color("green")
        turtle.left(30)
        draw_tree(3*l/4)
        turtle.right(60)
        draw_tree(3*l/4)
        turtle.left(30)
        turtle.backward(l)


draw_tree(100)

window.exitonclick()