import turtle
turt = turtle.Turtle()
turt.speed(200)
DISTANCE = 20

COLOR = ['red','yellow','green','blue','orange']

def colorstar(stop):
    turt.color(COLOR[stop % 5])
    turt.fd(DISTANCE + stop*10)
    turt.right(144)
    if stop == 0:
        turtle.done()
    else: 
        colorstar(stop - 1)

colorstar(18)