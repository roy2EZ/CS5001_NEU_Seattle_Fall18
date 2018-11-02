import turtle
turt = turtle.Turtle()
turt.speed(200)

#### PURPOSE
# To draw one side of a koch curve
#### SIGNATURE
# koch :: (Integer,Integer) => Void
#### TEMPLATE
# koch(given given…):
#    return returns
#### EXAMPLES
# koch(100,1) => 
# the graph will be the basic unit of koch curve, such as _/\_
# koch(100,2) => 
# the graph will be the curve's recursion on itself
# as a smaller triangle will be on each lines of the curve.

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
#### SIGNATURE
# snowflake :: (Integer,Integer,Integer) => Void
#### TEMPLATE
# snowflake(given given…):
#    return returns
#### EXAMPLES
# snowflake(3,200,4) => 
# the graph will be the snow flake with 3 sides of koch curve, 
# each one is 120 degree with each other, and in each unit koch curve, 
# there are 4 layers koch curve on itself.

def snowflake(n,size,order):
    for i in range(n):
        koch(size,order)
        turt.right(360/n)


#### Test: run the function to draw the snow flake
snowflake(3,200,4)
turtle.done()