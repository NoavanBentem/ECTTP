# Lab 8_0
class Ball(object):
    
    def __init__(self, xPos, yPos, xSpeed, ySpeed, radius):
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.radius = radius
     
           
    def display(self):
        ellipse(self.xPos,self.yPos,self.radius*2,self.radius*2)
        
    def move(self):
        self.xPos += self.xSpeed
        self.yPos += self.ySpeed
        
        if(self.xPos < self.radius or self.xPos > width- self.radius):
            self.xSpeed *= -1
        if(self.yPos < self.radius or self.yPos > height- self.radius):
            self.ySpeed *= -1
        