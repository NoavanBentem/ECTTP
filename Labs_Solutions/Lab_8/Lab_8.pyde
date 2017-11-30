#Oplossing Lab 8 - Valentijn Muijrers
from BallTab import Ball

def setup():
    size(800,600)
    
    global myBallsList
    myBallsList = []
    
    for i in range(10):
        radius = random(25,50)
        yPos = random(radius,height-radius)
        xPos = random(radius,width -radius)
        xSpeed = random(-5,5)
        ySpeed = random(-5,5)
        myBallsList.append(Ball(xPos, yPos, xSpeed,ySpeed,radius))
    

def draw():
    background(50)
    global myBallsList
    for i in range(0,len(myBallsList)):
        myBallsList[i].move()
        myBallsList[i].display()