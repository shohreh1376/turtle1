import turtle
import random
score=0
s=turtle.turtles()
s=turtle.Screen()
s.setup(600,600)
s.title('لاکپشت')
s.bgpic('./background.gif')
s.bgcolor("lightgreen")
wall=turtle.Turtle()
wall.up()
wall.goto(-275,275)
wall.down()
wall.width(4)
for i in range(4):
    wall.fd(550)
    wall.rt(90)
    wall.ht()
laki=turtle.Turtle()
laki.shape('turtle')
laki.color('green')
laki.shapesize(3)
laki.up()

ball=turtle.Turtle()
s.register_shape('./ball.gif')
#ball.shape('circle')
ball.shape('./ball.gif')
#ball.shapesize(3)
ball.color('yellow')
ball.up()
ball.goto(random.randint(-260,260),random.randint(-260,260))

wr=turtle.Turtle()
wr.up()
wr.goto(-270,275)
wr.ht()
wr.color('navy')
wr.write('amteaz='+str(score),font=('bkoodak',12,'bold'))


def move_right():
    laki.right(30)
def move_left():
    laki.left(30)
s.listen()
s.onkey(move_right,'Right')
s.onkey(move_left,'Left')

while True:
 laki.fd(1)
 if(laki.xcor() > 270  or laki.xcor() < -270 or laki.ycor() > 270 or laki.ycor()<-270):
           laki.right(180)
           score=score-5
           wr.clear()
           wr.write('amteaz='+str(score),font=('bkoodek',12,'bold'))
 if laki.distance(ball)<15:
           ball.goto(random.randint(-260,260),random.randint(-260,260))
           score=score+10
           wr.clear()
           wr.write('amteaz='+str(score), font=('bkoodek', 12, 'bold'))
 if score>=20:
           wr.goto(-75,0)
           wr.write('tanke you',font=('bboodek',25,'bold'))
           break
 



