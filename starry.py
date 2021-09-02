import turtle

a = turtle.Turtle()
a.speed(0)
a.width(2)
wn = turtle.Screen()
wn.bgcolor('black')
colors = ['', 'orange', 'yellow', 'green', 'blue', 'white', 'violet', 'red']


def star(n):
    for i in range(5):
        a.fd(n)
        a.rt(144)


for i in range(4):
    for i in range(8):

        a.color(colors[i % 8])
        star(i*40)
    a.lt(90)
turtle.done()
