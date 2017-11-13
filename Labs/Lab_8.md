## Lab 8: 
 

##### Grading Matrix 

Trait | Very Good | Good | Acceptable | Unsatisfactory	
--- |--- | --- | --- | --- |
| *Specifications* | The program produces correct results and meets all specifications. | The program works and produces the correct results and displays them correctly. It also meets most of the other specifications. | The program produces correct results but does not display them correctly. | The program is producing incorrect results.
*Readability* | The code is exceptionally well organized and very easy to follow. | The code is fairly easy to read. | The code is readable only by someone who knows what it is supposed to be doing.| The code is poorly organized and very difficult to read.|

##Bouncing Balls
##Exercise 8_0 

Make a class called Ball, and give it the following attributes: xPos, yPos, xSpeed, ySpeed, radius.
Also give the Ball class the following methods: def display(), and def move()
Implement the display-function so that it draws a circle on screen at position: xPos and yPos with size "radius".
Now create an object called myFirstBall in your setup function and call the display function on your object.
You should see a ball on your screen.

hint: if you forgot how to create a class, check the slides

##Exercise 8_1

Now implement the Move function which adds the xSpeed to the xPos and the ySpeed to the yPos of the ball.
Make sure it cannot leave the screen.

hint: to make sure the ball does not leave the screen, you can flip the xSpeed or ySpeed of the ball when it reaches the side of the screen.

##Exercise 8_2

In your setup-function, create a list called ballsList = [], and add 10 balls to your list.
In your draw-function, call the move function on all of the balls in the list, using a for-loop.

##INLEVEREN

##Put all of your code into a single sketch and zip your projectfolder, submit it online in the tool (check gi1718.hku.nl for the website).

Zipname:
ECTTP_homework_achternaam_voornaam_labnr.zip 
(voorbeeld: ECTTP_homework_muijrers_valentijn_7.zip )

##Due Date 

Turn each lab in 24 hours after the practicum.
