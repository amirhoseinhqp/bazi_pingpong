import turtle
sc = turtle.Screen()
sc.title("پینگ پونگ")
sc.bgcolor("white")
sc.setup(width=1000,height=600)

bazikon_meshki = turtle.Turtle()
bazikon_meshki.speed(10)
bazikon_meshki.shape("square")
bazikon_meshki.color("black")
bazikon_meshki.shapesize(stretch_wid=6,stretch_len=2)
bazikon_meshki.penup()
bazikon_meshki.goto(-400,0)

bazikon_ghermez = turtle.Turtle()
bazikon_ghermez.speed(10)
bazikon_ghermez.shape("square")
bazikon_ghermez.color("red")
bazikon_ghermez.shapesize(stretch_wid=6,stretch_len=2)
bazikon_ghermez.penup()
bazikon_ghermez.goto(400,0)

hit_ball = turtle.Turtle()
hit_ball.speed(80)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0,0)
hit_ball.dx = 5
hit_ball.dy = -5

#امتیاز
leftplayer= 0
rightplayer=0

# نمایش امتیاز
emtiaz = turtle.Turtle()
emtiaz.speed(0)
emtiaz.color("blue")
emtiaz.penup()
emtiaz.hideturtle()
emtiaz.goto(0,260)
emtiaz.write("بازیکن قرمز:0  بازیکن مشکی:0",align="center",font=("Courier",24,"normal"))

#تابع حرکت دادن پدال ها
def paddleup():
    y = bazikon_meshki.ycor()
    y += 20
    bazikon_meshki.sety(y)
  
def paddledown():
    y = bazikon_meshki.ycor()
    y -= 20
    bazikon_meshki.sety(y)
   
def paddleupr():
    y = bazikon_ghermez.ycor()
    y += 20
    bazikon_ghermez.sety(y)
  
def paddledownr():
    y = bazikon_ghermez.ycor()
    y -= 20
    bazikon_ghermez.sety(y)
  

#تنظیم دکمه های روی کیبورد
sc.listen()
sc.onkeypress(paddleup,"e")
sc.onkeypress(paddledown,"x")
sc.onkeypress(paddleupr,"Up")
sc.onkeypress(paddledownr,"Down")

while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

    #چک کردن عبور از خط
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
    if hit_ball.xcor() > 500:
        hit_ball.goto(0,0)
        hit_ball.dy *= -1
        leftplayer += 1
        emtiaz.clear()
        emtiaz.write("بازیکن قرمز:{}  بازیکن مشکی :{}".format(leftplayer,rightplayer),align="center",font=("Courier",24,"normal"))
    if hit_ball.xcor()<-500:
        hit_ball.goto(0,0)
        hit_ball.dy *= -1
        rightplayer +=1
        emtiaz.clear()
        emtiaz.write("بازیکن قرمز:{} بازیکن مشکی:{}".format(leftplayer,rightplayer),align="center",font=("Courier",24,"normal"))
        
    
    #برخورد توپ
    if (hit_ball.xcor() > 360 and
                        hit_ball.xcor() < 370) and\
                        (hit_ball.ycor() < bazikon_ghermez.ycor()+40 and
                        hit_ball.ycor() > bazikon_ghermez.ycor()-40): 
        hit_ball.setx(360) 
        hit_ball.dx*=-1
    
    if (hit_ball.xcor()<-360 and
    hit_ball.xcor()>-370) and\
    (hit_ball.ycor()<bazikon_meshki.ycor()+40 and
    hit_ball.ycor()>bazikon_meshki.ycor()-40):
         hit_ball.setx(-360)
         hit_ball.dx*=-1
        
    
    



