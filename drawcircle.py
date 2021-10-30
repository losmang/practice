import math
import turtle

# draw the circle using turtle
def draw_circle_turtle(x ,y , r):

    # move to the start of circle
    turtle.up()
    turtle.setpos()
    turtle.down()

    # draw the circle
    for i in range(0 , 365 , 5):
        a = math.radians(i)
        turtle.setpos(x + r *math.cos(a), y + r *math.sin(a))

    draw_circle_turtle(100 , 100 , 50)
    turtle.mainloop() 
