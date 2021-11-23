import turtle
t = turtle.Pen()

def rectangle(h,v,c):
    t.down()
    t.pensize(1)
    t.color(c)
    t.begin_fill()

    for i in range(2):
        t.forward(h)
        t.right(90)
        t.forward(v)
        t.right(90)
    t.end_fill()
    t.up()
    
#drawing the feet
t.up()
t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

#legs
t.goto(-25,-50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

#arms
