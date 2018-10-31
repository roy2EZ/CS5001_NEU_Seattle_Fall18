import turtle
turt = turtle.Turtle()
turt.speed(200)

#### PURPOSE
# To draw one side of a koch curve
#### Signature
# koch :: (Integer,Integer) => Graph
#### Template
# koch(given given…):
#### EXAMPLES
# koch(100,1) => __/\__
def koch(size,order):
    if order <= 0:
        turt.fd(size)
    else:
        koch(size/3,order-1)
        turt.left(60)
        koch(size/3,order-1)
        turt.left(-120)
        koch(size/3,order-1)
        turt.left(60)
        koch(size/3,order-1)
        
#### PURPOSE
# To draw the full koch snowflake
#### Signature
# snowflake :: (Integer,Integer,Integer) => Graph
#### Template
# snowflake(given given…):
           
def snowflake(n,size,order):
    for i in range(n):
        koch(size,order)
        turt.right(360/n)


#### Test

snowflake(3,200,3)
turtle.done()