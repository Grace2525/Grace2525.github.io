import turtle as t
import random as r
import time
import os
t.bgcolor("purple")
t.speed(0)
bglist=['green','sky blue','pink','purple','gray','black']
def drawButten(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
def writeText(x,y,color,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.write(text,align="center",font=("simsun",30,"normal"))
def startGame():
    global leftNumber,rightNumber,computerJudge
    drawButten(0,0,"red")
    drawButten(-50,0,"blue")
    drawButten(-50,-50,"gray")
    drawButten(0,-50,"gray")
    writeText(0,200,"yellow","争分夺秒")
    writeText(-25,-45,"white","对")
    writeText(25,-45,"white","错")
    writeText(0,-95,"white","退出")
    leftNumber=r.randint(1,100)
    rightNumber=r.randint(1,100) 
    writeText(-50,125,"white",leftNumber)
    writeText(50,125,"white",rightNumber)
    assertation=['左边小','右边大','右边小','左边大']
    computerJudge=r.choice(assertation)
    writeText(0,60,"white",computerJudge)
startGame()
def checkAnther(x,y):
    judge=0
    if leftNumber<rightNumber:
        if computerJudge=='左边小' or computerJudge=='右边大':
            if -50<=x<=0:
                judge=True
            else:
                judge=False
        else:
            if -50<=x<=0:
                judge=False
            else:
                judge=True         
    else:
        if computerJudge=='左边小' or computerJudge=='右边大':
            if -50<=x<=0:
                judge=False
            else:
                judge=True
        else:
            if -50<=x<=0:
                judge=True
            else:
                judge=False        
    return judge
def writeAnswer(x,y):
    isClickButten(x,y)
    if click!=None:
        if click==True:
            anther=checkAnther(x,y)
            if anther:
                tRight.forward(250)
                writeText(0,-150,"orange","答对了")
                time.sleep(1)
                t.clear()
                startGame()
            else:
                tRight.backward(75)
                writeText(0,-150,"orange","答错了")
                time.sleep(1)
                t.clear()
                startGame()
        else:
            writeText(0,-150,"orange","请点击按钮")
            time.sleep(1)
            t.undo()
    else:
        os._exit(0)
t.onscreenclick(writeAnswer)
def isClickButten(x,y):
    global click
    if -50<=x<=50:
        if -50<=y<=0:
            click=True
        elif -100<=y<=-50:
            click=None
    else:
        clike=False
    return click
tRight=t.clone()
tRight.color("white")
tRight.penup()
tRight.goto(350,-300)
tRight.left(90)
tRight.shape("turtle")
tRight.shapesize(4)
def fall():
    tRY=tRight.ycor()
    if -550<=tRY<=550:
        tRight.backward(10)
    elif tRY<-550:
        t.clear() 
        writeText(0,0,"yellow","----游戏失败----")
        time.sleep(1)
        t.clear()
        tRight.goto(350,-300)
    else:
        t.clear()
        writeText(0,0,"yellow","----游戏胜利----")
        time.sleep(1)
        t.clear()
        tRight.goto(350,-300)
    t.ontimer(fall,300)
fall()
def changeColor():
    bg=r.choice(bglist)
    t.bgcolor(bg)
    t.ontimer(changeColor,1000)
changeColor()
