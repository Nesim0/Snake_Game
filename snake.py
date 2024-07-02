import turtle
import time
import random
speed = 0.15
window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('lightgreen')
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,100)
head.setheading = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,0)
food.shapesize(0.80, 0.80)

tail = []
point = 0
write = turtle.Turtle()
write.speed(0)
write.shape('square')
write.color('white')
write.penup()
write.goto(0,260)
write.hideturtle()
write.write('Point: {}' .format(point), align='center', font=('Courier',24,'normal'))


def move():
    if head.setheading == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.setheading == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.setheading == 'right':
        x = head.xcor()
        head.setx(x+20)
    if head.setheading == 'left':
        x = head.xcor()
        head.setx(x-20)

def goUp():
    if head.setheading != 'down':
        head.setheading = 'up'
def goDown():
    if head.setheading != 'up':
        head.setheading = 'down'

def goRight():
    if head.setheading != 'left':
        head.setheading = 'right'
def goLeft():
    if head.setheading != 'right':
        head.setheading = 'left'


window.listen()
window.onkey(goUp, 'Up')
window.onkey(goDown, 'Down')
window.onkey(goRight, 'Right')
window.onkey(goLeft, 'Left')

while True:
    window.update()
    for segment in tail:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in tail:
                segment.goto(1000, 1000)
            tail = []
            point = 0
            write.clear()
            write.write('point: {}'.format(point), align='center', font=('Courier', 24, 'normal'))
            speed = 0.15
    if head.xcor()> 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0,0)
        head.setheading ='stop'
        for tails in tail:
            tails.goto(1000,1000)
        tail =[]
        speed = 0.15
        point = 0
        write.clear()
        write.write('Point: {}' .format(point), align='center', font=('Courier',24,'normal'))
    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x,y)
        point = point + 10
        write.clear()
        write.write('Point: {}' .format(point), align='center', font=('Courier',24,'normal'))
        speed = speed-0.01
        newTail= turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('white')
        newTail.penup()
        tail.append(newTail)
    
    for i in range(len(tail)- 1, 0, -1):
        x = tail[i - 1].xcor()
        y = tail[i - 1].ycor()
        tail[i].goto(x,y)
    if len(tail)> 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x,y)
    move()
    time.sleep(speed)